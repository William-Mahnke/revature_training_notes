# Week 2 - Review Questions

The following are specific questions related to concepts covered in Week 2 of training. If you are able to confidently answer the questions in this review guide, you should be able to confidently answer any question related to the week 2 material.

## NumPy

**What is an ndarray?**

**How does NumPy achieve better performance than pure Python for numerical operations?**

**What is the difference between a 1D and a 2D NumPy array?**

**Name three mathematical functions provided by NumPy.**

**Why is NumPy considered foundational to the Python data science ecosystem?**

**How would you create a 3x3 array of zeros using NumPy?**

**What is an ndarray and how does it differ from a Python list in terms of memory layout?**

**What does it mean for a NumPy array to be homogeneous and why does this matter?**

**Name three Python libraries that are built on top of NumPy.**

**What is the conventional alias used when importing NumPy?**

**How do you install NumPy using pip?**

**Why is it recommended to install NumPy inside a virtual environment?**

**What is the difference between np.arange() and np.linspace()?**

**What does arr.shape return and what does it tell you?**

**What is boolean masking and how do you use it to filter an array?**

**What does np.reshape() do and what rule must be followed when reshaping?**

**Name four statistical functions provided by NumPy.**

**Why is a 2D array a natural fit for storing student scores across multiple subjects?**

**What does the axis parameter control in functions like np.mean()?**

**What is the difference between axis=0 and axis=1 when calculating the mean?**

**What does np.argmax() return? Provide an example of how it can be used.**

**What is normalisation and how is it performed using vectorised NumPy operations?**

## Pandas: Basics

**What is Pandas and what is it primarily used for?**

**What is the difference between a Series and a DataFrame?**

**How is a DataFrame similar to a spreadsheet or SQL table?**

**How would you load a CSV file into a Pandas DataFrame?**

**How would you filter a DataFrame to show only rows where a column meets a condition?**

**What library does Pandas build on top of and why?**

**What are the two core data structures in Pandas and how do they differ?**

**How does a DataFrame relate to a Series?**

**What does it mean for Pandas to work with labelled data and why is this an advantage?**

**How does Pandas differ from NumPy in terms of the data it is designed to handle?**

**Why should Pandas be installed inside a virtual environment?**

**What is the conventional import alias for Pandas?**

**How do you verify that Pandas has been installed correctly?**

## Pandas: Selecting and Inspecting Data

**What is the difference between df.loc[] and df.iloc[]?**

**What do df.info() and df.describe() each show you?**

**How do you filter rows in a DataFrame using a condition?**

**How do you combine multiple filter conditions in Pandas?**

**What is the difference between selecting a single column and selecting multiple columns from a DataFrame in terms of what type is returned?**

**What does df.dtypes tell you and why does it matter?**

**What is the first thing you should do after loading a dataset into a DataFrame and why?**

**Why is it important to explore a dataset before transforming or analysing it and what kinds of problems can be caught at this stage?**

**What is the difference between df.head() and df.sample() and when might you prefer one over the other?**

## Pandas: Loading and Saving Data

**How do you save a DataFrame to a CSV file and how do you read one back in?**

**What does pd.read_csv() always return?**

**What does the parse_dates parameter do and why is it useful?**

**What is the purpose of na_values and when would you need to use it?**

**What does index=False do in df.to_csv() and what happens if you omit it?**

**What is the chunksize parameter and in what situation would you reach for it?**

**Why is exporting a cleaned dataset a useful final step in a data pipeline?**

## Pandas: Working with JSON

**What is the orient parameter in pd.read_json() and why is it necessary?**

**Which orient value is most commonly returned by REST APIs and why does it map cleanly to a DataFrame?**

**What problem arises when loading nested JSON directly into a DataFrame and which pandas function is used to address it?**

**What do the record_path and meta parameters of pd.json_normalize() do?**

**What is newline-delimited JSON (NDJSON) and in what kind of data engineering context would you commonly encounter it?**

**Why is JSON larger on disk than CSV for equivalent data and what implication does this have for large-scale pipelines?**

**You receive an API response where each record contains a nested location object with state and sales_office as sub-keys. How would you flatten this into a standard DataFrame?**

## Pandas: Cleaning Data

**What is the difference between df.dropna() and df.fillna()?**

**What is the difference between df.dropna() and df.dropna(subset=["column"])?**

**Why is it important to remove duplicate rows before performing analysis?**

**How would you calculate null counts as a percentage of total rows rather than as raw counts?**

**Why is it important to understand why a null exists before deciding how to handle it?**

**What is the difference between fillna() and replace() and when would you use each?**

**Why is .str.strip() considered one of the most important text cleaning steps even when the data looks clean at first glance?**

**What is the difference between .str.contains() and .str.extract() and when would you use each?**

**Why is building familiarity with regular expressions a worthwhile investment for a Data Engineer working with text data?**

## Pandas: Grouping, Reshaping, and Combining Data

**What does df.groupby() do and what pattern does it implement?**

**How does df.groupby().agg() differ from df.groupby().sum()?**

**What does df.merge() do and what is the equivalent operation in SQL?**

**What is the difference between an inner join and a left join and what data loss risk does using an inner join introduce?**

**What is the difference between wide format and long format data and which is generally preferred for storage in a data pipeline?**

**What is the difference between df.pivot() and df.pivot_table()?**

**What is df.melt() and in what situation would you need to use it?**

**What do the id_vars and value_vars parameters of melt() control?**

**What is the relationship between stack() and unstack() and what type does stack() return?**

## Pandas: Working with Dates

**What does df["order_date"].dt.month do and why must the column be a datetime type first?**

**Why is it important to ensure a date column is stored as datetime64 rather than as a string and what are two ways to achieve this when loading a CSV?**

**What is the .dt accessor and what kinds of properties does it expose on a datetime column?**

## Matplotlib

**What is Matplotlib?**

**What is the difference between a Figure and an Axes in Matplotlib?**

**How do you install Matplotlib using pip?**

**Why must plt.savefig() be called before plt.show()?**

**What happens if you run a script that creates a plot but does not call plt.show()?**

**Which chart type is most appropriate for showing a trend over time?**

**What is the difference between a bar chart and a histogram?**

**What does plt.subplots() return and how do you plot onto a specific panel?**

**What does plt.tight_layout() do and when is it most useful?**

**What does the alpha parameter control in a scatter plot?**

**Why is visualisation described as the final step in a data pipeline rather than a cosmetic addition?**

**What does a scatter plot reveal that other chart types do not and what kind of data does it require?**

**What does a histogram show and how does it differ from a bar chart?**

**You want to compare total quantity sold per department across four months simultaneously. Which chart type would you use and how would you prepare the data first?**

**Why is choosing the right chart type important beyond just aesthetics?**

**What are the minimum formatting steps a chart should have before being shared with a stakeholder?**

**What does the alpha parameter control and when is it particularly useful?**

**What are the four linestyle options available in Matplotlib?**

**What is the difference between plt.title() and ax.set_title() and which style is preferred when working with multiple subplots?**

**What does plt.tight_layout() do and what problem does it prevent?**

**What does plt.subplots(2, 2) return and how do you access the individual Axes objects in a 2x2 grid?**

## FastAPI

**What is FastAPI and what two core libraries is it built on? What does each provide?**

**What is Uvicorn and what role does it play when running a FastAPI application?**

**How does FastAPI use Python type annotations and what three things do they drive automatically?**

**What is Swagger UI and how is it made available in a FastAPI application?**

**Why is FastAPI particularly well suited to I/O-bound workloads compared to traditional synchronous frameworks?**

**What is Uvicorn's role in a FastAPI application and how does it differ from the application itself?**

**What does the --reload flag do and why should it not be used in production?**

**What is the difference between a def and async def path operation function and when should each be used?**

**What does the tags parameter on a route decorator do?**

**What are the five core HTTP method decorators in FastAPI and what operation does each represent?**

**What is the difference between a path parameter and a query parameter? How does FastAPI distinguish between them?**

**How do you make a query parameter optional in FastAPI and what happens if a required query parameter is missing from a request?**

**What is the difference between PUT and PATCH and when would you use each?**

**How would you define a route that accepts both a path parameter and an optional query parameter?**

**How does FastAPI know that a function parameter represents a request body rather than a path or query parameter?**

**What does response_model do and why is its filtering behaviour important for security?**

**What is HTTPException and how does it differ from simply returning an error message in the response body?**

**What is APIRouter and what problem does it solve as a FastAPI project grows?**

**How is a router registered on the main app instance and what does that registration do?**

**Why is it better to raise HTTPException than to return a plain dictionary containing an error message?**

## Consuming APIs with httpx

**What is the difference between httpx.AsyncClient and httpx.Client and when should each be used?**

**What does raise_for_status() do and what would happen if you omitted it?**

**Why is httpx preferred over requests in a FastAPI application and in what situation would requests still be acceptable?**

**Why is it important to use httpx.AsyncClient as a context manager rather than instantiating it directly?**

## Pydantic

**What is Pydantic and what problem does it solve that Python's built-in type hints do not?**

**What happens when you pass invalid data to a Pydantic model and what information does the error provide?**

**What is type coercion in the context of Pydantic and can you give an example of when it occurs?**

**What is the difference between a required field and an optional field in a Pydantic model?**

**What does model_dump() return and when would you use it?**

**What does Field() add to a Pydantic field beyond its type annotation and give three examples of constraints it can express?**

**What is the difference between @field_validator and @model_validator and when would you use each?**

**What is a nested Pydantic model and how does Pydantic handle validation of nested data?**

**How does Pydantic handle Python Enum types and what validation does it apply automatically?**

**Why should API keys never be hardcoded in source code?**
