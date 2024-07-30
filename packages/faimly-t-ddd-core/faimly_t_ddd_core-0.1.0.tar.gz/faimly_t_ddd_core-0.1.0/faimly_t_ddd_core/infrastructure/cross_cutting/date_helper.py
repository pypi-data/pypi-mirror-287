from datetime import datetime
import pytz

class DateHelper:
    date_formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%S",
        "%d/%m/%Y %H:%M:%S"
    ]

    @staticmethod
    def parse_date_time(p_date_time: str) -> datetime:
        for date_format in DateHelper.date_formats:
            try:
                return datetime.strptime(p_date_time, date_format).replace(tzinfo=pytz.UTC)
            except ValueError:
                continue
        raise ValueError("Invalid date format.")

    @staticmethod
    def get_date_time_utc(p_date_time: datetime) -> datetime:
        if p_date_time.tzinfo is None:
            return pytz.UTC.localize(p_date_time)
        return p_date_time.astimezone(pytz.UTC)

    @staticmethod
    def convert_to_pst(p_date_time: datetime) -> datetime:
        date_time_utc = DateHelper.get_date_time_utc(p_date_time)
        pst_time_zone = pytz.timezone('US/Pacific')
        return date_time_utc.astimezone(pst_time_zone)

    @staticmethod
    def convert_to_str(p_date_time: datetime, format: str = None) -> str:
        if not format:
            format = "%Y-%m-%d %H:%M:%S"
        return p_date_time.strftime(format)
