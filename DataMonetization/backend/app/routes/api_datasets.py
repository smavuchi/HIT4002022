from app.helpers.router import router

router.make_class(
  name="api dataset routes",
  url_prefix="/dataset",
  classes=["specific resource routes"]
  )
router.make_class(
  name="specific dataset routes",
  # url_prefix="/<string:dataset_id>",
  classes=["api dataset routes"]
  )

## 

router.make_route(
  name="get dataset data",
  url="/data",
  classes=["api dataset routes", "retrieval routes"],
  description="get dataset data"
  )

router.make_route(
  name="add a dataset",
  url="",
  classes=["api dataset routes", "creation routes"],
  description="adds a new API dataset"
  )

router.make_route(
  name="delete an api dataset",
  url="",
  classes=["specific dataset routes", "deletion routes"],
  description="deletes an API dataset"
  )

router.make_route(
  name="get an api dataset",
  url="",
  classes=["specific dataset routes", "retrieval routes"],
  description="retrieves an API dataset"
  )

router.make_route(
  name="download a dataset",
  url="/download",
  classes=["specific dataset routes", "retrieval routes"],
  description="downloads the API dataset"
  )

## dataset-info routes
router.make_class(
  name="dataset-info routes",
  url_prefix="/info",
  classes=["specific dataset routes", "retrieval routes"]
  )

router.make_route(
  name="get dataset columns",
  url="/columns",
  classes=["dataset-info routes", "retrieval routes"],
  description="retrieves dataset columns"
  )

router.make_route(
  name="get numeric dataset columns",
  url="/columns/numeric",
  classes=["dataset-info routes", "retrieval routes"],
  description="retrieves numeric dataset columns"
  )

router.make_route(
  name="get nonnumeric dataset columns",
  url="/columns/nonnumeric",
  classes=["dataset-info routes", "retrieval routes"],
  description="retrieves nonnumeric dataset columns"
  )

router.make_route(
  name="retrieve value counts for columns",
  url="/column-value-counts",
  classes=["dataset-info routes", "retrieval routes"],
  description="retrieves value counts for columns"
  )

router.make_route(
  name="retrieve missing values by column",
  url="/missing-values/column-wise",
  classes=["dataset-info routes", "retrieval routes"],
  description="retrieves missing values by column"
  )

router.make_route(
  name="retrieve missing values by row",
  url="/missing-values/row-wise",
  classes=["dataset-info routes", "retrieval routes"],
  description="retrieves missing values by row"
  )

router.make_route(
  name="get dataset issues",
  url="/issues",
  classes=["dataset-info routes", "retrieval routes"],
  description="retrieves issues found in the dataset"
  )

## cleaning routes
router.make_class(
  name="cleaning routes",
  url_prefix="/resolve",
  classes=["specific dataset routes", "creation routes"]
  )

router.make_route(
  name="set column types",
  url="/column-types",
  classes=["cleaning routes"],
  description="sets column types in the dataset. Note: types are as follows: \
      i - integer, \
      b - boolean, \
      u - unsigned integer, \
      f - float, \
      c - complex float, \
      m - timedelta, \
      M - datetime, \
      O - object, \
      S - string, \
      U - unicode string, \
      V - fixed chunk of memory for other type ( void )"
  )

router.make_route(
  name="set columns",
  url="/columns",
  classes=["cleaning routes"],
  description="sets required columns in the dataset"
  )

router.make_route(
  name="set id columns",
  url="/id-columns",
  classes=["cleaning routes"],
  description="sets id columns in the dataset"
  )

router.make_route(
  name="resolve duplicate rows",
  url="/duplicates",
  classes=["cleaning routes"],
  description="resolves duplicate rows. To be specific, it keeps the first one and drops the rest"
  )

router.make_route(
  name="resolve inconsistent data",
  url="/inconsistent-data",
  classes=["cleaning routes"],
  description="resolves inconsistent data. To be specific, inconsistent capitalization and whitespace"
  )

router.make_route(
  name="resolve missing data by dropping columns",
  url="/missing-data/drop-columns",
  classes=["cleaning routes"],
  description="resolve missing data by dropping columns"
  )

router.make_route(
  name="resolve missing data by dropping rows",
  url="/missing-data/drop-rows",
  classes=["cleaning routes"],
  description="resolve missing data by dropping rows"
  )

router.make_route(
  name="resolve missing data by inserting defaults",
  url="/missing-data/insert-defaults",
  classes=["cleaning routes"],
  description="resolve missing data by inserting defaults"
  )

router.make_route(
  name="resolve missing data by inserting medians",
  url="/missing-data/insert-medians",
  classes=["cleaning routes"],
  description="resolve missing data by inserting medians"
  )

router.make_route(
  name="resolve missing data by inserting frequent values",
  url="/missing-data/insert-frequent-values",
  classes=["cleaning routes"],
  description="resolve missing data by inserting frequent values"
  )