create datetime from string

    from dateutils.parser import parse
    parse("20160901")

create date ranges

    import pandas as pd
    pd.date_range(start, end)

format dates

    x = parse("20160901")
    x.strftime("%Y-%m-%d")

subtract date range

  from datetime import timedelta
  d = datetime.today() - timedelta(days=days_to_subtract)

  from datetime.relativedelta import relativedelta
  d = datetime.today() - timedelta(months=3)
