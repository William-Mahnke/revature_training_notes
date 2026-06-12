# ═══════════════════════════════════════════════════════
# Mocking — Real World Example
# ═══════════════════════════════════════════════════════
# This file demonstrates a realistic mocking scenario using
# a layered application structure:
#
#   Employee        — the domain model (data object)
#   EmployeeService — the service layer (database access)
#   BusinessLogic   — the business logic layer (what we test)
#
# The key principle: we want to test the BusinessLogic class
# in isolation, without involving a real database. We achieve
# this by mocking the EmployeeService — replacing it with a
# controlled fake that we can configure and inspect.
#
# This means our tests are:
#   Fast       — no real database queries
#   Repeatable — no dependency on external state
#   Focused    — only the business logic is under test
#
# spec= is passed to Mock() to constrain it to only allow
# attributes and methods that exist on the real class, preventing
# accidentally passing tests due to misspelled method names.
# ═══════════════════════════════════════════════════════
import unittest
from unittest.mock import Mock

# --- Employee Model Class ---
# A plain data object representing an employee record.
# In a real application this might be an ORM model or a dataclass.
class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, department={self.department}, salary={self.salary})"


# --- Service Layer (the real service — not used in tests) ---
# Represents the data access layer. In a real application, these
# methods would execute database queries. They are defined here
# to establish the interface that BusinessLogic depends on.
# The NotImplementedError clearly signals these are not meant to
# be called directly in tests.
class EmployeeService:
    def get_employee(self, employee_id):
        # In reality, this would query a database
        raise NotImplementedError("Connects to a real database")

    def get_all_employees(self):
        # In reality, this would query a database
        raise NotImplementedError("Connects to a real database")

    def save_employee(self, employee):
        # In reality, this would query a database
        raise NotImplementedError("Connects to a real database")

    def delete_employee(self, employee_id):
        # In reality, this would query a database
        raise NotImplementedError("Connects to a real database")


# --- Facsimile of our Business Logic Layer (what we actually want to test) ---
# This class contains the real logic we are testing. It depends on
# EmployeeService to retrieve and persist data, but does not care
# about the implementation — it only calls the service's interface.
# This makes it straightforward to inject a mock service in tests.
class BusinessLogic:
    def __init__(self, service):
        self.service = service

    def get_employee_name(self, employee_id):
        # Calls the service to retrieve an employee, then returns their name.
        # Tests verify: (1) the correct name is returned, and (2) the service
        # was called with the correct employee_id.
        employee = self.service.get_employee(employee_id)
        return employee.name

    def get_department_employees(self, department):
        # Retrieves all employees from the service, then filters by department.
        # The filtering logic is what we are testing here — the service call
        # itself is mocked to return a controlled list.
        all_employees = self.service.get_all_employees()
        return [e for e in all_employees if e.department == department]

    def give_raise(self, employee_id, amount):
        # Retrieves an employee, applies the raise, and saves the updated record.
        # Tests verify: (1) the correct updated salary is returned, and (2) the
        # service's save_employee method was called with the updated employee.
        employee = self.service.get_employee(employee_id)
        employee.salary += amount
        self.service.save_employee(employee)
        return employee.salary

    def fire_employee(self, employee_id):
        # Retrieves an employee and deletes them unless they are in the Executive
        # department — in which case a PermissionError is raised.
        # Tests verify: (1) delete is called for non-executives, (2) PermissionError
        # is raised for executives, and (3) delete is NOT called for executives.
        employee = self.service.get_employee(employee_id)
        if employee.department == "Executive":
            raise PermissionError("Executive employees cannot be removed this way.")
        self.service.delete_employee(employee_id)


# --- Tests ---
class TestEmployeeApplication(unittest.TestCase):

    def setUp(self):
        # Setup the Mocked Service, our Business logic to test, and some dummy employee objects

        # Mock the service layer — no database required.
        # 'spec' is passed to only allow attributes and methods that exist on
        # the real EmployeeService class. This prevents accidentally calling
        # a misspelled method and passing a test.
        self.mock_service = Mock(spec=EmployeeService)

        # This is the class actually under test - we pass our mock service to this
        # class, so that we can control the potential calls to databases/APIS/etc...
        # BusinessLogic receives the mock service via constructor injection —
        # it behaves identically to the real service from BusinessLogic's perspective.
        self.logic = BusinessLogic(self.mock_service)

        # Reusable test employees — created once in setUp and shared across tests.
        # These are real Employee instances, not mocks, because the business logic
        # interacts with their attributes (name, salary, department).
        self.employee_alice = Employee(1, "Alice Johnson", "Engineering", 60000)
        self.employee_bob   = Employee(2, "Bob Smith",     "Engineering", 55000)
        self.employee_carol = Employee(3, "Carol White",   "Executive",   95000)

    # --- get_employee_name ---

    def test_get_employee_name_returns_correct_name(self):
        # Configures the mock to return a specific employee, then verifies
        # that get_employee_name() returns their name correctly.
        # Tests all three employees to cover different name values.
        self.mock_service.get_employee.return_value = self.employee_alice
        result = self.logic.get_employee_name(1)
        self.assertEqual(result, "Alice Johnson")

        self.mock_service.get_employee.return_value = self.employee_bob
        result = self.logic.get_employee_name(2)
        self.assertEqual(result, "Bob Smith")

        self.mock_service.get_employee.return_value = self.employee_carol
        result = self.logic.get_employee_name(3)
        self.assertEqual(result, "Carol White")

    def test_get_employee_name_calls_service_with_correct_id(self):
        # Verifies behaviour: that get_employee_name() passes the correct
        # employee_id to the service. This tests the interaction, not just
        # the return value — confirming the right ID is forwarded.
        self.mock_service.get_employee.return_value = self.employee_alice
        self.logic.get_employee_name(1)
        self.mock_service.get_employee.assert_called_once_with(1)

    # --- get_department_employees ---

    def test_get_department_employees_returns_correct_subset(self):
        # Configures the mock to return all three employees, then verifies
        # that filtering by "Engineering" returns only Alice and Bob.
        # Tests both that the correct employees ARE included in the result.
        self.mock_service.get_all_employees.return_value = [
            self.employee_alice,
            self.employee_bob,
            self.employee_carol
        ]
        result = self.logic.get_department_employees("Engineering")
        self.assertEqual(len(result), 2)
        self.assertIn(self.employee_alice, result)
        self.assertIn(self.employee_bob, result)

    def test_get_department_employees_excludes_other_departments(self):
        # Complements the above test by verifying that Carol (Executive)
        # is NOT included in Engineering results. Testing exclusion separately
        # makes failures easier to diagnose.
        self.mock_service.get_all_employees.return_value = [
            self.employee_alice,
            self.employee_bob,
            self.employee_carol
        ]
        result = self.logic.get_department_employees("Engineering")
        self.assertNotIn(self.employee_carol, result)

    # --- give_raise ---

    def test_give_raise_returns_updated_salary(self):
        # Verifies the return value: that give_raise() returns the new salary
        # after the raise has been applied (60000 + 5000 = 65000).
        self.mock_service.get_employee.return_value = self.employee_alice
        new_salary = self.logic.give_raise(1, 5000)
        self.assertEqual(new_salary, 65000)

    def test_give_raise_calls_save_employee(self):
        # Verifies behaviour: that give_raise() calls save_employee() on the
        # service after applying the raise — ensuring the update is persisted.
        # assert_called_once_with() checks both that it was called and the argument.
        self.mock_service.get_employee.return_value = self.employee_alice
        self.logic.give_raise(1, 5000)
        self.mock_service.save_employee.assert_called_once_with(self.employee_alice)

    # --- fire_employee ---

    def test_fire_employee_calls_delete_on_service(self):
        # Verifies that firing a non-executive employee calls delete_employee()
        # on the service with the correct employee_id.
        self.mock_service.get_employee.return_value = self.employee_bob
        self.logic.fire_employee(2)
        self.mock_service.delete_employee.assert_called_once_with(2)

    def test_fire_executive_raises_permission_error(self):
        # Verifies that attempting to fire an Executive employee raises a
        # PermissionError — testing the guard clause in fire_employee().
        self.mock_service.get_employee.return_value = self.employee_carol
        with self.assertRaises(PermissionError):
            self.logic.fire_employee(3)

    def test_fire_executive_does_not_call_delete(self):
        # Verifies that when a PermissionError is raised for an Executive,
        # delete_employee() is never called on the service.
        # The try/except swallows the expected PermissionError so the test
        # can proceed to assert that delete was not called.
        # assert_not_called() confirms delete_employee() was never invoked.
        self.mock_service.get_employee.return_value = self.employee_carol
        try:
            self.logic.fire_employee(3)
        except PermissionError:
            pass
        self.mock_service.delete_employee.assert_not_called()
