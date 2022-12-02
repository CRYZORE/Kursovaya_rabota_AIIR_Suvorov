from django.db import models

# Create your models here.
class Replacer:
    def __init__(self, first_operand, result):
        self.first_operand = first_operand
        self.result = result
        self.operation = 'replace'