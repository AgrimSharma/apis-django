# coding=utf-8
# length for how long process occurred
basic = [
      "Less than 1 min",
      "1-2 mins",
      "3-5 mins",
      "more than 5 mins"
    ]

normal = [
    "Less than 1 min",
    "1-5 mins",
    "5-30 mins",
    "~an hour",
    "several hours",
    "constant",
    "comes and goes"
    ]

extreme = [
    "~an hour",
    "several hours",
    "a day",
    "several days"
]

length = dict(angina=basic,
              pain_in_body=normal,
              shortness_ofbreath=normal,
              swelling=extreme
              )
