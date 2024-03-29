from rest_framework import serializers
from first_app.models import CarSpecs


class CarSpecsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarSpecs
        fields = ['id', 'car_brand', 'car_model',
                  'production_year', 'car_body', 'engine_type']