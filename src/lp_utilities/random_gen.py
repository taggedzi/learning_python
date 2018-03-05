#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def random_signed_float(magnitude):
    return random.random() * random.randint(-magnitude, magnitude)


def random_signed_integer(magnitude):
    return random.randint(-magnitude, magnitude)


def random_signed_complex(magnitude):
    return complex(0, random.random() * random.randint(-magnitude, magnitude))
