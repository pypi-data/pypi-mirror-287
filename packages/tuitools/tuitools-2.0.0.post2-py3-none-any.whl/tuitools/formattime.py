def formattime_now(ymd,hms):
    from datetime import datetime
    now=datetime.now()
    formatted_time = now.strftime("%Y"+ymd+'%m'+ymd+'%d %H'+hms+'%M'+hms+'%S')
    print(formatted_time)