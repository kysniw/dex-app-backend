from rest_framework import serializers
from .models import (AdditionalOption, SillWidth, SillCategory, SillThickness, SillCategory, WindowSill)


class AdditonalOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalOption
        fields = '__all__'
        read_only_fields = ['id']


class SillWidthSerializer(serializers.ModelSerializer):

    class Meta:
        model = SillWidth
        fields = '__all__'
        read_only_fields = ['id']


class SillThicknessSerializer(serializers.ModelSerializer):

    class Meta:
        model = SillThickness
        fields = '__all__'
        read_only_fields = ['id']


class SillCategorySerializer(serializers.ModelSerializer):

    additional_options = AdditonalOptionSerializer(many = True, required = False)

    class Meta:
        model = SillCategory
        fields = '__all__'
        read_only_fields = ['id']


class SillCategorySmallSerializer(serializers.ModelSerializer):

    class Meta:
        model = SillCategory
        fields = ['id', 'category_name', 'manufacturer']


class WindowSillSerializer(serializers.ModelSerializer):

    width_option = SillWidthSerializer(many = True, required = False)
    thickness_option = SillThicknessSerializer(many = True, required = False)
    sill_category = SillCategorySerializer(many = False, required = True)

    class Meta:
        model = WindowSill
        fields = '__all__'
        read_only_fields = ['id']


class WindowSillListSerializer(serializers.ModelSerializer):

    sill_category = SillCategorySmallSerializer(many = False, required = True)

    class Meta:
        model = WindowSill
        fields = ['id', 'sill_category', 'color_name', 'image']