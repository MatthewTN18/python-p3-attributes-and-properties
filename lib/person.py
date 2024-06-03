#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Jobless"):
        self.name = name
        self.job = job

    def get_name(self):
        return self.name

    def set_name(self, name):
        if not isinstance(name, str):
            print("Name must be between 1 and 25 characters.")
        elif not name:
            print("Name must be between 1 and 25 characters.")
        elif not (1 <= len(name) <= 25):
            print("Name must be between 1 and 25 characters.")
        else:
            self.name = name
     
    def get_job(self):
        return self.job

    def set_job(self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")




