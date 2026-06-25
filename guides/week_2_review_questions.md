# Week 2 - Review Questions

The following are specific questions related to concepts covered in Week 2 of training. If you are able to confidently answer the questions in this review guide, you should be able to confidently answer any question related to the week 2 material.

## NumPy

**What is an ndarray?**

- An ndarray (n-dimensional array) is NumPy's core data structure: a grid of values of the same data type, which can have any number of dimensions (1D vectors, 2D matrices, etc.). It is created with functions like `np.array([1, 2, 3])`.

**How does NumPy achieve better performance than pure Python for numerical operations?**

- NumPy stores data in contiguous blocks of memory and runs its operations as vectorised, pre-compiled C code rather than slow, interpreted Python loops. This means numerical operations are applied to the whole array at once, avoiding the overhead of looping element-by-element in Python.

**What is the difference between a 1D and a 2D NumPy array?**

- A 1D array is a single sequence of values (like a list), e.g. `np.array([1, 2, 3])`. A 2D array is a grid of values arranged into rows and columns (like a table or matrix), e.g. `np.array([[1, 2, 3], [4, 5, 6]])`.

**Name three mathematical functions provided by NumPy.**

- `np.sum()`, `np.mean()`, and `np.std()` (others include `np.min()`, `np.max()`, and `np.median()`).

**Why is NumPy considered foundational to the Python data science ecosystem?**

- Many of the most widely used data science libraries (such as Pandas, Matplotlib, and scikit-learn) are built on top of NumPy and use its ndarray as their underlying data structure. Its efficient, homogeneous arrays provide the performance and common foundation the rest of the ecosystem depends on.

**How would you create a 3x3 array of zeros using NumPy?**

- `np.zeros((3, 3))` — passing the shape as a tuple creates a 3x3 array filled with `0.0`.

**What is an ndarray and how does it differ from a Python list in terms of memory layout?**

- An ndarray is NumPy's n-dimensional array. Unlike a Python list (which stores pointers to objects scattered throughout memory), an ndarray stores its elements of a single fixed type in one contiguous block of memory, which makes access and vectorised operations far faster.

**What does it mean for a NumPy array to be homogeneous and why does this matter?**

- Homogeneous means every element in the array is of the same data type (its `dtype`). This matters because it allows NumPy to store the data compactly in contiguous memory and run fast, vectorised C operations over it without checking the type of each element.

**Name three Python libraries that are built on top of NumPy.**

- Pandas, Matplotlib, and scikit-learn.

**What is the conventional alias used when importing NumPy?**

- `np`, i.e. `import numpy as np`.

**How do you install NumPy using pip?**

- `pip install numpy`.

**Why is it recommended to install NumPy inside a virtual environment?**

- A virtual environment isolates project dependencies and their versions, preventing conflicts between projects and keeping the global Python installation clean. This makes the project reproducible since each project can pin the exact package versions it needs.

**What is the difference between np.arange() and np.linspace()?**

- `np.arange(start, stop, step)` generates evenly spaced values defined by a step size (the stop value is excluded), e.g. `np.arange(0, 10, 2)` → `[0 2 4 6 8]`. `np.linspace(start, stop, num)` generates a specified number of evenly spaced values between two endpoints (the endpoint is included by default), e.g. `np.linspace(0, 1, 5)` → `[0. 0.25 0.5 0.75 1.]`.

**What does arr.shape return and what does it tell you?**

- It returns a tuple giving the size of the array along each dimension. For example a 3-row, 4-column array returns `(3, 4)`, telling you it has 3 rows and 4 columns.

**What is boolean masking and how do you use it to filter an array?**

- Boolean masking applies a condition to an array to produce an array of `True`/`False` values, which is then used to select only the elements where the condition is `True`. For example, `arr[arr > 50]` returns only the elements of `arr` greater than 50.

**What does np.reshape() do and what rule must be followed when reshaping?**

- `np.reshape()` changes the shape (dimensions) of an array without changing its data. The rule is that the total number of elements must stay the same — the product of the new dimensions must equal the original number of elements (e.g. a 12-element array can be reshaped to `(3, 4)` or `(2, 6)` but not `(3, 3)`).

**Name four statistical functions provided by NumPy.**

- `np.mean()`, `np.median()`, `np.std()`, and `np.percentile()` (others include `np.sum()`, `np.min()`, and `np.max()`).

**Why is a 2D array a natural fit for storing student scores across multiple subjects?**

- A 2D array maps naturally onto rows and columns — for example each row can represent a student and each column a subject. This layout also lets you compute statistics along a chosen axis, such as each student's average (per row) or each subject's average (per column).

**What does the axis parameter control in functions like np.mean()?**

- It controls the direction along which the operation is applied. Without it, the function operates over the entire array; with it, the function collapses a specific dimension (axis) and returns a result per row or per column.

**What is the difference between axis=0 and axis=1 when calculating the mean?**

- `axis=0` operates down the rows, collapsing them to give a result per column (the mean of each column). `axis=1` operates across the columns, collapsing them to give a result per row (the mean of each row).

**What does np.argmax() return? Provide an example of how it can be used.**

- It returns the index (position) of the maximum value in an array rather than the value itself. For example, given `scores = np.array([55, 70, 95, 63])`, `np.argmax(scores)` returns `2`, which could be used to identify which student or item achieved the highest score.

**What is normalisation and how is it performed using vectorised NumPy operations?**

- Normalisation rescales data to a common range (commonly 0 to 1) so values can be compared on the same scale. Using vectorised operations it is done across the whole array at once, e.g. min-max normalisation: `(arr - arr.min()) / (arr.max() - arr.min())`.

## Pandas: Basics

**What is Pandas and what is it primarily used for?**

- Pandas is a Python library for working with structured, tabular data. It is primarily used for loading, cleaning, transforming, and analysing data, providing labelled data structures (the Series and DataFrame) that make manipulating real-world datasets convenient.

**What is the difference between a Series and a DataFrame?**

- A Series is a one-dimensional labelled array (a single column of data with an index). A DataFrame is a two-dimensional labelled table made up of multiple columns — essentially a collection of Series sharing the same index.

**How is a DataFrame similar to a spreadsheet or SQL table?**

- Like a spreadsheet or SQL table, a DataFrame organises data into rows and columns where each column has a name and a data type, and each row represents a record. You can select columns, filter rows, and run aggregations much like you would in a spreadsheet or with SQL queries.

**How would you load a CSV file into a Pandas DataFrame?**

- Use `pd.read_csv()`, e.g. `df = pd.read_csv("sales_data.csv")`.

**How would you filter a DataFrame to show only rows where a column meets a condition?**

- Use boolean masking by passing a condition in square brackets, e.g. `df[df["unit_price"] > 50]` returns only the rows where `unit_price` is greater than 50.

**What library does Pandas build on top of and why?**

- Pandas is built on top of NumPy. It uses NumPy's fast, contiguous ndarray to store column data internally, which gives Pandas efficient, vectorised numerical operations as its foundation.

**What are the two core data structures in Pandas and how do they differ?**

- The Series and the DataFrame. A Series is one-dimensional (a single labelled column), while a DataFrame is two-dimensional (a labelled table of multiple columns sharing one index).

**How does a DataFrame relate to a Series?**

- A DataFrame is essentially a collection of Series that share a common index — each column of a DataFrame is a Series. Selecting a single column from a DataFrame (e.g. `df["unit_price"]`) returns a Series.

**What does it mean for Pandas to work with labelled data and why is this an advantage?**

- Pandas attaches labels to data via row indexes and column names rather than relying solely on integer positions. This is an advantage because you can select, align, and combine data by meaningful labels, which makes code clearer and reduces errors when joining or aligning datasets.

**How does Pandas differ from NumPy in terms of the data it is designed to handle?**

- NumPy is designed for homogeneous numerical data in n-dimensional arrays. Pandas is designed for heterogeneous, labelled tabular data — different columns can hold different data types (numbers, strings, dates), with named columns and a row index.

**Why should Pandas be installed inside a virtual environment?**

- Installing Pandas in a virtual environment isolates it (and its dependencies like NumPy) to the project, avoiding version conflicts with other projects and keeping the global Python installation clean and the project reproducible.

**What is the conventional import alias for Pandas?**

- `pd`, i.e. `import pandas as pd`.

**How do you verify that Pandas has been installed correctly?**

- Import it and check its version, e.g. run `python -c "import pandas as pd; print(pd.__version__)"`. If it imports and prints a version without error, the installation is working.

## Pandas: Selecting and Inspecting Data

**What is the difference between df.loc[] and df.iloc[]?**

- `df.loc[]` is label-based — it selects rows and columns by their index labels and column names (and label slices are inclusive of the endpoint). `df.iloc[]` is position-based — it selects by integer position (like a list index), and slices exclude the endpoint.

**What do df.info() and df.describe() each show you?**

- `df.info()` shows structural information: the number of rows, the columns, their data types, and the non-null count per column (which reveals missing values). `df.describe()` shows summary statistics (count, mean, std, min, quartiles, max) for the numeric columns by default.

**How do you filter rows in a DataFrame using a condition?**

- Pass a boolean condition inside square brackets, e.g. `df[df["state"] == "Colorado"]` returns only the rows where `state` equals "Colorado".

**How do you combine multiple filter conditions in Pandas?**

- Combine conditions with the bitwise operators `&` (and) and `|` (or), wrapping each condition in parentheses, e.g. `df[(df["state"] == "Colorado") & (df["department"] == "Electronics")]`.

**What is the difference between selecting a single column and selecting multiple columns from a DataFrame in terms of what type is returned?**

- Selecting a single column with `df["col"]` returns a Series. Selecting multiple columns with a list, e.g. `df[["col1", "col2"]]`, returns a DataFrame.

**What does df.dtypes tell you and why does it matter?**

- `df.dtypes` reports the data type of each column (e.g. `int64`, `float64`, `object`, `datetime64[ns]`). It matters because the dtype determines which operations are valid — for instance, date columns stored as `object` (strings) won't support time-based operations until converted to `datetime64`.

**What is the first thing you should do after loading a dataset into a DataFrame and why?**

- Inspect it — typically with `df.head()`, `df.info()`, and `df.describe()`. This confirms the data loaded correctly and reveals its shape, column types, and missing values before you start transforming or analysing it.

**Why is it important to explore a dataset before transforming or analysing it and what kinds of problems can be caught at this stage?**

- Exploring first lets you understand the data's structure and spot quality issues early. You can catch problems such as missing/null values, incorrect data types, duplicate rows, inconsistent categorical values (typos, inconsistent casing/whitespace), and outliers — all of which would otherwise corrupt downstream analysis.

**What is the difference between df.head() and df.sample() and when might you prefer one over the other?**

- `df.head(n)` returns the first n rows in order, while `df.sample(n)` returns n randomly selected rows. `head()` is convenient for a quick first look, but `sample()` is less biased because it draws from across the whole dataset, which can reveal issues not visible in just the top rows (e.g. if the data is sorted).

## Pandas: Loading and Saving Data

**How do you save a DataFrame to a CSV file and how do you read one back in?**

- Save with `df.to_csv("file.csv", index=False)` and read back with `df = pd.read_csv("file.csv")`.

**What does pd.read_csv() always return?**

- A DataFrame.

**What does the parse_dates parameter do and why is it useful?**

- `parse_dates` tells Pandas to convert the listed columns into `datetime64` while loading, e.g. `pd.read_csv("sales_data.csv", parse_dates=["sale_date"])`. It is useful because it produces proper datetime columns at load time, saving a separate conversion step and enabling date/time operations immediately.

**What is the purpose of na_values and when would you need to use it?**

- `na_values` specifies additional strings that should be treated as missing/null values, e.g. `na_values=["N/A", "unknown", "-", ""]`. You need it when a dataset represents missing data with placeholder text that Pandas wouldn't otherwise recognise as null.

**What does index=False do in df.to_csv() and what happens if you omit it?**

- `index=False` stops Pandas from writing the DataFrame's row index as an extra column in the output file. If you omit it, the default index is written out, adding an unwanted extra column that reappears when the file is read back in.

**What is the chunksize parameter and in what situation would you reach for it?**

- `chunksize` makes `pd.read_csv()` return an iterator that yields the file in chunks of that many rows at a time instead of loading it all at once. You reach for it when a file is too large to fit comfortably in memory, so you can process it piece by piece.

**Why is exporting a cleaned dataset a useful final step in a data pipeline?**

- Exporting saves the cleaned, transformed data so the expensive cleaning work doesn't have to be repeated. The output becomes a reliable, reusable artefact that downstream steps, tools, or teammates can consume directly.

## Pandas: Working with JSON

**What is the orient parameter in pd.read_json() and why is it necessary?**

- `orient` tells Pandas how the JSON is structured (e.g. `"records"`, `"columns"`, `"index"`) so it knows how to map the JSON into rows and columns. It is necessary because JSON can represent the same tabular data in several different layouts, and Pandas needs to know which one it is reading to reconstruct the DataFrame correctly.

**Which orient value is most commonly returned by REST APIs and why does it map cleanly to a DataFrame?**

- `"records"` — a list of objects like `[{"product_id": "PRD-054", ...}, {...}]`. It maps cleanly because each object becomes a row and each key becomes a column, which mirrors a DataFrame's row/column structure directly.

**What problem arises when loading nested JSON directly into a DataFrame and which pandas function is used to address it?**

- When JSON contains nested objects, loading it directly leaves whole sub-objects (dicts) stuffed into single columns instead of being broken out into their own columns. `pd.json_normalize()` is used to flatten the nested structure into a proper flat table.

**What do the record_path and meta parameters of pd.json_normalize() do?**

- `record_path` specifies the path to the nested list of records that should become the rows of the DataFrame. `meta` specifies fields from the parent/outer level to keep and repeat alongside each of those records, so context from the higher level isn't lost when flattening.

**What is newline-delimited JSON (NDJSON) and in what kind of data engineering context would you commonly encounter it?**

- NDJSON is a format where each line is a separate, self-contained JSON object (rather than one big array). It is written/read with `lines=True`. You commonly encounter it in logs, event streams, and streaming/big-data pipelines, where records can be appended and processed one line at a time.

**Why is JSON larger on disk than CSV for equivalent data and what implication does this have for large-scale pipelines?**

- JSON repeats the field names (keys) for every single record and includes extra structural characters (braces, quotes, colons), whereas CSV lists column names only once in a header. This redundancy makes JSON larger, which at scale means higher storage costs and slower I/O — so columnar/compressed formats (like Parquet) are often preferred for large pipelines.

**You receive an API response where each record contains a nested location object with state and sales_office as sub-keys. How would you flatten this into a standard DataFrame?**

- Use `pd.json_normalize(api_response)`, which flattens nested keys using dot notation, producing columns such as `location.state` and `location.sales_office`. You can then rename those columns (e.g. `df.rename(columns={"location.state": "state", "location.sales_office": "sales_office"})`) for cleaner names.

## Pandas: Cleaning Data

**What is the difference between df.dropna() and df.fillna()?**

- `df.dropna()` removes rows (or columns) that contain null values. `df.fillna()` keeps those rows but replaces the null values with a specified value (e.g. a default, a computed mean/median, or values mapped from another column).

**What is the difference between df.dropna() and df.dropna(subset=["column"])?**

- `df.dropna()` drops a row if any column in it is null. `df.dropna(subset=["column"])` is scoped — it only drops rows where the specified column(s) are null, ignoring nulls in other columns.

**Why is it important to remove duplicate rows before performing analysis?**

- Duplicate rows double-count records, which skews aggregates such as sums, counts, and averages and produces misleading results. Removing them (with `df.drop_duplicates()`) ensures each record is counted once so the analysis reflects the true data.

**How would you calculate null counts as a percentage of total rows rather than as raw counts?**

- Divide the null counts by the number of rows and multiply by 100, e.g. `(df.isnull().sum() / len(df) * 100).round(2)`.

**Why is it important to understand why a null exists before deciding how to handle it?**

- The reason a value is missing determines the correct fix. Some nulls can be reliably inferred from other columns (e.g. deriving `state` from `sales_office`), some should be filled with a sensible statistic (e.g. a median price), and some genuinely indicate a missing record that should be dropped. Blindly dropping or filling without understanding the cause can introduce bias or destroy valid data.

**What is the difference between fillna() and replace() and when would you use each?**

- `fillna()` specifically targets null/`NaN` values and substitutes a value for them. `replace()` swaps out specified existing values for new ones (e.g. fixing typos or standardising categories like `"Colroado"` → `"Colorado"`). Use `fillna()` for handling missing data and `replace()` for correcting/standardising known values.

**Why is .str.strip() considered one of the most important text cleaning steps even when the data looks clean at first glance?**

- Leading or trailing whitespace is invisible to the eye but breaks operations like grouping, joining, and equality comparisons — `"Colorado "` won't match `"Colorado"`. `.str.strip()` removes that hidden whitespace so values match and group correctly.

**What is the difference between .str.contains() and .str.extract() and when would you use each?**

- `.str.contains()` returns a boolean mask indicating which rows contain a given substring/pattern — used for filtering rows (e.g. offices containing "Colorado"). `.str.extract()` pulls out and returns the matched portion(s) of a string via a regex capture group — used to create new data from text (e.g. extracting the numeric part of `PRD-054`).

**Why is building familiarity with regular expressions a worthwhile investment for a Data Engineer working with text data?**

- Regular expressions provide a powerful, concise way to search, validate, extract, and clean text patterns that are extremely common in real-world data (IDs, dates, codes, inconsistent formatting). Many Pandas string methods (`.str.contains()`, `.str.extract()`, `.str.replace()`) accept regex, so knowing them greatly expands what you can do when cleaning and transforming text columns.

## Pandas: Grouping, Reshaping, and Combining Data

**What does df.groupby() do and what pattern does it implement?**

- `df.groupby()` splits the data into groups based on the values of one or more columns, applies an aggregation to each group, and combines the results. It implements the "split-apply-combine" pattern, e.g. `df.groupby("department")["quantity"].sum()` totals quantity per department.

**How does df.groupby().agg() differ from df.groupby().sum()?**

- `df.groupby().sum()` applies a single fixed aggregation (sum) to the groups. `df.groupby().agg()` is more flexible — it lets you apply one or more named aggregations, and even different functions to different columns, in a single call (e.g. `.agg(total="sum", average="mean", count="count")`).

**What does df.merge() do and what is the equivalent operation in SQL?**

- `df.merge()` combines two DataFrames by matching rows on one or more key columns. The equivalent SQL operation is a JOIN.

**What is the difference between an inner join and a left join and what data loss risk does using an inner join introduce?**

- An inner join keeps only rows that have a matching key in both DataFrames. A left join keeps all rows from the left DataFrame and fills in nulls where the right has no match. The risk with an inner join is data loss: any left-side rows without a match in the right table are silently dropped from the result.

**What is the difference between wide format and long format data and which is generally preferred for storage in a data pipeline?**

- In wide format, each variable/category has its own column (e.g. a column per month), making it compact for display. In long format, there are fewer columns with one row per observation (e.g. columns like `department`, `month`, `quantity`). Long format is generally preferred for storage and processing in pipelines because it is more flexible, easier to filter/group, and scales better as new categories appear.

**What is the difference between df.pivot() and df.pivot_table()?**

- `df.pivot()` reshapes data from long to wide and requires the index/column combinations to be unique — it raises an error if duplicates exist. `df.pivot_table()` also reshapes long to wide but can aggregate duplicate combinations using an `aggfunc` (e.g. `sum`, `mean`), so it handles non-unique data.

**What is df.melt() and in what situation would you need to use it?**

- `df.melt()` reshapes data from wide to long format, collapsing multiple columns into key/value pairs. You'd use it when you have a wide table (e.g. one column per month) and need a long, tidy form for analysis, plotting, or storage — essentially the reverse of a pivot.

**What do the id_vars and value_vars parameters of melt() control?**

- `id_vars` lists the columns to keep as fixed identifier columns (repeated for each row). `value_vars` lists the columns to unpivot into the new variable/value pair; if omitted, all columns not in `id_vars` are melted.

**What is the relationship between stack() and unstack() and what type does stack() return?**

- They are inverse operations: `stack()` moves column labels down into the row index (wide → long), while `unstack()` moves an index level back out into columns (long → wide). `stack()` returns a Series with a MultiIndex.

## Pandas: Working with Dates

**What does df["order_date"].dt.month do and why must the column be a datetime type first?**

- It extracts the month (as an integer 1–12) from each date in the `order_date` column. The column must be a datetime type first because the `.dt` accessor and its date components are only available on `datetime64` columns — on a string column they aren't defined.

**Why is it important to ensure a date column is stored as datetime64 rather than as a string and what are two ways to achieve this when loading a CSV?**

- Stored as a string, a date can't be used for time-based operations (extracting components, filtering by date, resampling, sorting chronologically); as `datetime64` all of those work. Two ways to achieve it when loading a CSV: (1) pass `parse_dates=["sale_date"]` to `pd.read_csv()`, or (2) load normally and then convert with `pd.to_datetime(df["sale_date"])`.

**What is the .dt accessor and what kinds of properties does it expose on a datetime column?**

- The `.dt` accessor provides access to the datetime components and methods of a `datetime64` Series. It exposes properties such as `.year`, `.month`, `.month_name()`, `.day`, `.day_name()`, `.quarter`, and similar, allowing you to pull out parts of each date.

## Matplotlib

**What is Matplotlib?**

- Matplotlib is a Python library for creating static, data visualisations and plots — line charts, bar charts, scatter plots, histograms, and more. Its `pyplot` interface (conventionally imported as `plt`) is the standard tool for charting in the Python data ecosystem.

**What is the difference between a Figure and an Axes in Matplotlib?**

- A Figure is the overall canvas/container for the whole image, which can hold one or more plots. An Axes is an individual plot (a single set of x/y axes) drawn within the Figure — the actual area where data is plotted. One Figure can contain multiple Axes (subplots).

**How do you install Matplotlib using pip?**

- `pip install matplotlib`.

**Why must plt.savefig() be called before plt.show()?**

- `plt.show()` renders and then clears/closes the current figure, so calling `savefig()` afterwards would save a blank image. Calling `plt.savefig()` first ensures the populated figure is written to file before it is displayed and cleared.

**What happens if you run a script that creates a plot but does not call plt.show()?**

- In a plain script the chart is never displayed — the figure is built in memory but no window opens. (In a Jupyter notebook, charts render inline without `plt.show()`, but a standalone script requires it to show the plot.)

**Which chart type is most appropriate for showing a trend over time?**

- A line chart.

**What is the difference between a bar chart and a histogram?**

- A bar chart compares a value across distinct categories (one bar per category, with gaps between bars). A histogram shows the distribution of a single numeric variable by grouping values into bins and showing how many fall into each, so its bars are adjacent and represent continuous ranges rather than separate categories.

**What does plt.subplots() return and how do you plot onto a specific panel?**

- It returns a tuple of `(figure, axes)`. With multiple panels, `axes` is an array, and you plot onto a specific panel by indexing it, e.g. `ax[0].bar(...)` or `ax[0, 1].plot(...)` for a grid.

**What does plt.tight_layout() do and when is it most useful?**

- It automatically adjusts spacing between plot elements so titles, axis labels, and tick labels don't overlap or get cut off. It is most useful when a figure has multiple subplots or long/rotated labels.

**What does the alpha parameter control in a scatter plot?**

- `alpha` controls the transparency of the markers (0 = fully transparent, 1 = fully opaque). Lower values help reveal density where many points overlap, since overlapping translucent points appear darker.

**Why is visualisation described as the final step in a data pipeline rather than a cosmetic addition?**

- Visualisation is how the results of all the preceding work (loading, cleaning, transforming, analysing) are communicated and made actionable. It turns processed data into insight that stakeholders can understand and make decisions from, so it is the delivery point of the pipeline rather than mere decoration.

**What does a scatter plot reveal that other chart types do not and what kind of data does it require?**

- A scatter plot reveals the relationship or correlation between two numeric variables (and clusters/outliers in that relationship). It requires two continuous numeric columns, one for each axis.

**What does a histogram show and how does it differ from a bar chart?**

- A histogram shows the distribution of a single numeric variable by dividing its range into bins and showing the frequency (count) in each bin. It differs from a bar chart in that its bars represent continuous numeric ranges (and sit adjacent with no gaps), whereas a bar chart compares discrete, separate categories.

**You want to compare total quantity sold per department across four months simultaneously. Which chart type would you use and how would you prepare the data first?**

- Use a grouped bar chart. Prepare the data by grouping by month and department and summing quantity, then reshaping it to wide format (e.g. `df.groupby([month, "department"])["quantity"].sum().unstack()`) so each month has a group of bars with one bar per department.

**Why is choosing the right chart type important beyond just aesthetics?**

- The chart type determines how accurately and clearly the data's message is conveyed. The wrong type can hide patterns or actively mislead the viewer (e.g. using a line chart for unrelated categories implies a trend that isn't there), whereas the right type matches the data and the question, making the insight obvious and correct.

**What are the minimum formatting steps a chart should have before being shared with a stakeholder?**

- At minimum it should have a descriptive title, clearly labelled x and y axes (with units where relevant), and a legend when multiple series are shown. Applying `plt.tight_layout()` so nothing overlaps or is cut off is also part of making it presentable.

**What does the alpha parameter control and when is it particularly useful?**

- `alpha` controls transparency (0 = transparent, 1 = opaque). It is particularly useful on scatter plots with many overlapping points, where transparency reveals density, and for layering elements so underlying detail remains visible.

**What are the four linestyle options available in Matplotlib?**

- Solid (`"-"`), dashed (`"--"`), dash-dot (`"-."`), and dotted (`":"`).

**What is the difference between plt.title() and ax.set_title() and which style is preferred when working with multiple subplots?**

- `plt.title()` uses the stateful pyplot interface and sets the title on the "current" Axes. `ax.set_title()` uses the object-oriented interface and sets the title on a specific Axes object explicitly. The `ax.set_title()` style is preferred with multiple subplots because it targets each panel unambiguously.

**What does plt.tight_layout() do and what problem does it prevent?**

- It automatically adjusts the padding and spacing between plot elements. It prevents overlapping or clipped titles, axis labels, and tick labels, which is especially common when figures have multiple subplots or rotated/long labels.

**What does plt.subplots(2, 2) return and how do you access the individual Axes objects in a 2x2 grid?**

- It returns a Figure and a 2x2 NumPy array of Axes objects. You access individual panels with two indices, e.g. `ax[0, 0]`, `ax[0, 1]`, `ax[1, 0]`, `ax[1, 1]` (or iterate over them using `ax.flatten()`).

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
