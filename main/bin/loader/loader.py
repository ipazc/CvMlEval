#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Iván de Paz Centeno'


class Loader(object):
    def __init__(self, modules):
        self.modules = modules

    def get_module(self, module_id):
        return self.modules[module_id]

    def does_module_exist(self, module_id):
        return module_id in self.modules

    def get_available_modules(self):
        result = []
        for k,v in self.modules.items():
            result.append(k)

        return result

    def __str__(self):
        return "\n".join(str("\t" + x) for x in self.get_available_modules())
