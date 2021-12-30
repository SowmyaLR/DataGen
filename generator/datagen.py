from faker import Faker
import datetime

fk = Faker()


class NUMBER:
    def __init__(self):
        self.min = None
        self.max = None

    def _less_than(self, value):
        if not self.max or value < self.max:
            self.max = value - 1

    def _less_than_or_equal(self, value):
        if not self.max or value < self.max:
            self.max = value

    def _greater_than(self, value):
        if not self.min or value > self.min:
            self.min = value + 1

    def _greater_than_or_equal(self, value):
        if not self.min or value > self.min:
            self.min = value

    def _equal_to(self, value):
        self.min = value
        self.max = value

    def _frame_rule(self, schema):
        for cnd, value in schema["Conditions"].items():
            getattr(self, "_%s" % cnd.lower())(value)

    def generate(self, schema):
        if "Conditions" in schema:
            self._frame_rule(schema)
        return self._generate_data()

    def _generate_data(self):
        if self.min and self.max:
            return fk.random_int(self.min, self.max)
        elif self.min and not self.max:
            return fk.random_int(min=self.min, max=self.min * 10)
        elif not self.min and self.max:
            return fk.random_int(max=self.max)
        else:
            return fk.random_int()



class TEXT:
    def _name_(self):
        return fk.name()

    def _fname_(self):
        return fk.first_name()

    def _lname_(self):
        return fk.last_name()

    def _email_(self):
        return fk.email()

    def ip_address(self):
        return fk.ip_address()

    def _job_role(self):
        return fk.job()

    def _address(self):
        return fk.address()

    def _url(self):
        return fk.url()

    def _color(self):
        return fk.color_name()

    def generate(self, schema):
        return getattr(self, "_%s", schema["SubType"].lower())



class DATE:
    def __init__(self, schema):
        self.schema = schema

    def _past_date(self):
        return fk.past_date()

    def _future_date(self):
        return fk.future_date()

    def _date_between(self):
        st_date = datetime.datetime.date(datetime.datetime.strptime(self.schema["start_date"], '%Y-%m-%d'))
        end_dt = datetime.datetime.date(datetime.datetime.strptime(self.schema["end_date"], '%Y-%m-%d'))
        return fk.date_between(start_date=st_date, end_date=end_dt)

    def _random_date(self):
        return fk.date_between()

# class DateTime:
#     def __init__(self, schema):
#         self.schema = schema
#
#     def _past_date_time(self):
#         return fk.past_date_time()
#
#     def _future_date_time(self):
#         return fk.futire_date_time()
#
#     def _date_time_between(self):
#         st =

class Generator:
    def __init__(self, schema):
        self.schema = schema
