from factory import Factory, Faker
from pss_project.api.models.rest.metrics.MicrobenchmarkMetrics import MicrobenchmarkMetrics


class MicrobenchmarkMetricsFactory(Factory):
    class Meta:
        model = MicrobenchmarkMetrics

    throughput = Faker('pydecimal', left_digits=9, right_digits=15, positive=True)
    tolerance = Faker('random_int')
    iterations = Faker('random_int')
    status = Faker('random_element', elements=('PASS', 'FAIL'))
    ref_throughput = Faker('pydecimal', left_digits=9, right_digits=15, positive=True)
    stdev_throughput = Faker('pydecimal', left_digits=9, right_digits=15, positive=True)
