from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Package


@registry.register_document
class PackageDocument(Document):
    class Index:
        name = 'package'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = Package
        fields = [
            'flight_number',
            'hotel_name',
            'tour_operator',
            'airline'
        ]
