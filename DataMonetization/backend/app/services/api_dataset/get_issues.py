from app.services.api_dataset.get_dataframe import get_dataframe

def find_duplicate_rows(df, ignore=[]):
  return int(df[df.drop(columns=ignore).duplicated(keep="first")].shape[0])


def get_columns_with_min_percentage_repetition(df, value):
  columns = []
  num_rows = len(df)

  for col in df.columns:
    cnts = df[col].value_counts(dropna=False)
    top_pct = (cnts/num_rows).iloc[0]

    if top_pct > value/100:
      columns.append(col)

  return columns

def get_percentage_missing_values_by_column(df, as_dict=False):
  result = df.isna().mean()
  return result if not as_dict else dict(result)

def get_columns_missing_all_values(df):
  missing_values = get_percentage_missing_values_by_column(df, True)
  values = [x for x in missing_values if missing_values[x] > 0.09]
  return values

def get_rows_missing_most_values(df, _min=80):
  missing = df.isna().sum(axis='columns')
  rows = 0

  for item in dict(missing):
    if missing[item] > int((_min/100) * len(df.columns)):
      rows += item

  return rows

def get_rows_with_whitespace_issues(df):
  rows_init = int(tuple(df.shape)[0])

  for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].str.strip()

  rows_after = int(tuple(df.shape)[0])
  return rows_init - rows_after 

def get_rows_with_whitespace_issues(df):
  rows_init = int(tuple(df.shape)[0])

  for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].str.strip()

  rows_after = int(tuple(df.shape)[0])
  return rows_init - rows_after 

def get_columns_with_capitalization_issues(df):
  columns = set()

  for column in df.select_dtypes(include=['object']).columns:
    og = dict(df[column].value_counts())
    df[column] = df[column].str.lower()
    now = dict(df[column].value_counts())

    for value in og:
      new_val = int(now[value.lower()])
      old_val = int(og[value])
      if old_val != new_val:
        columns.add(column)

  return len(columns)

def get_columns_with_potential_outliers(df):
  columns = 0
  kurt = dict(df.kurt(numeric_only=True)[:10])
  
  for column in kurt:
    if kurt[column] > 4:
      columns += 1

  return columns

def get_dataset_issues(dataset):
  df = get_dataframe(dataset)

  # duplicated records
  ignore_columns = (["id"] if "id" in df.columns else []) + [x for x in dataset.id_columns if x in df.columns]
  duplicated_rows = find_duplicate_rows(df, ignore_columns)

  # useless columns
  # - 100% duplicated values
  columns_with_same_values = len(get_columns_with_min_percentage_repetition(df, 100))

  # - 100% missing values
  columns_missing_all_values = len(get_columns_missing_all_values(df))

  # useless rows
  # - 80% missing values
  rows_missing_most_values = get_rows_missing_most_values(df, _min=80)

  # inconsistent data
  # -- whitespace
  rows_with_whitespace_issues = get_rows_with_whitespace_issues(df)

  # -- capitalization
  columns_with_capitalization_issues = get_columns_with_capitalization_issues(df)

  # columns with potential outliers
  columns_with_potential_outliers = get_columns_with_potential_outliers(df)

  return {
    "duplicated_rows": duplicated_rows,
    "columns_with_same_values": columns_with_same_values,
    "columns_missing_all_values": columns_missing_all_values,
    "rows_missing_most_values": rows_missing_most_values,
    "rows_with_whitespace_issues": rows_with_whitespace_issues,
    "columns_with_capitalization_issues": columns_with_capitalization_issues,
    "columns_with_potential_outliers": columns_with_potential_outliers
  }