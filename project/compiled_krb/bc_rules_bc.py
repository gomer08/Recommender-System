# bc_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def place_agency_landlines(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'hotline', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.place_agency_landlines: got unexpected plan from when clause 1"
            with engine.prove('facts', 'region', context,
                              (rule.pattern(3),
                               rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_rules.place_agency_landlines: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def place_agency_specific(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'hotline', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.place_agency_specific: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def place_agency_all_landlines(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'hotline', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.place_agency_all_landlines: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def plan_action_label(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'action', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.plan_action_label: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def place_evac(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'evac_area', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.place_evac: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def place_region(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'region', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.place_region: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def place_quotes(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'quote', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.place_quotes: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def place_org(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'org', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.place_org: got unexpected plan from when clause 1"
            with engine.prove('facts', 'region', context,
                              (rule.pattern(2),
                               rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_rules.place_org: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def get_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'suggest', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.get_action: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def place_situation(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'situational', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.place_situation: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def place_coords(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'coords', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.place_coords: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_rules')
  
  bc_rule.bc_rule('place_agency_landlines', This_rule_base, 'place_agency',
                  place_agency_landlines, None,
                  (contexts.variable('location'),
                   contexts.variable('number'),
                   contexts.variable('agency'),),
                  (),
                  (contexts.variable('region'),
                   contexts.variable('number'),
                   contexts.variable('agency'),
                   contexts.variable('location'),))
  
  bc_rule.bc_rule('place_agency_specific', This_rule_base, 'place_specific',
                  place_agency_specific, None,
                  (contexts.variable('location'),
                   contexts.variable('number'),
                   contexts.variable('agency'),),
                  (),
                  (contexts.variable('location'),
                   contexts.variable('number'),
                   contexts.variable('agency'),))
  
  bc_rule.bc_rule('place_agency_all_landlines', This_rule_base, 'place_agency_all_location',
                  place_agency_all_landlines, None,
                  (contexts.variable('location'),
                   contexts.variable('number'),
                   contexts.variable('agency'),),
                  (),
                  (contexts.variable('location'),
                   contexts.variable('number'),
                   contexts.variable('agency'),))
  
  bc_rule.bc_rule('plan_action_label', This_rule_base, 'plan_action',
                  plan_action_label, None,
                  (contexts.variable('label'),
                   contexts.variable('action'),),
                  (),
                  (contexts.variable('label'),
                   contexts.variable('action'),))
  
  bc_rule.bc_rule('place_evac', This_rule_base, 'place_evac_region',
                  place_evac, None,
                  (contexts.variable('city'),
                   contexts.variable('center'),),
                  (),
                  (contexts.variable('city'),
                   contexts.variable('center'),))
  
  bc_rule.bc_rule('place_region', This_rule_base, 'place_region',
                  place_region, None,
                  (contexts.variable('place'),
                   contexts.variable('region'),),
                  (),
                  (contexts.variable('place'),
                   contexts.variable('region'),))
  
  bc_rule.bc_rule('place_quotes', This_rule_base, 'place_inspirational_quotes',
                  place_quotes, None,
                  (contexts.variable('num'),
                   contexts.variable('q'),),
                  (),
                  (contexts.variable('num'),
                   contexts.variable('q'),))
  
  bc_rule.bc_rule('place_org', This_rule_base, 'place_org',
                  place_org, None,
                  (contexts.variable('location'),
                   contexts.variable('org'),),
                  (),
                  (contexts.variable('region'),
                   contexts.variable('org'),
                   contexts.variable('location'),))
  
  bc_rule.bc_rule('get_action', This_rule_base, 'get_action_suggest',
                  get_action, None,
                  (contexts.variable('word'),
                   contexts.variable('update'),),
                  (),
                  (contexts.variable('word'),
                   contexts.variable('update'),))
  
  bc_rule.bc_rule('place_situation', This_rule_base, 'place_situation',
                  place_situation, None,
                  (contexts.variable('signal'),
                   contexts.variable('situation'),),
                  (),
                  (contexts.variable('signal'),
                   contexts.variable('situation'),))
  
  bc_rule.bc_rule('place_coords', This_rule_base, 'place_coords',
                  place_coords, None,
                  (contexts.variable('lat'),
                   contexts.variable('long'),
                   contexts.variable('city'),),
                  (),
                  (contexts.variable('lat'),
                   contexts.variable('long'),
                   contexts.variable('city'),))


Krb_filename = '..\\bc_rules.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 27), (4, 4)),
    ((28, 34), (5, 5)),
    ((47, 51), (8, 8)),
    ((53, 60), (10, 10)),
    ((73, 77), (13, 13)),
    ((79, 86), (15, 15)),
    ((99, 103), (18, 18)),
    ((105, 111), (20, 20)),
    ((124, 128), (23, 23)),
    ((130, 136), (25, 25)),
    ((149, 153), (28, 28)),
    ((155, 161), (30, 30)),
    ((174, 178), (33, 33)),
    ((180, 186), (35, 35)),
    ((199, 203), (38, 38)),
    ((205, 211), (40, 40)),
    ((212, 218), (41, 41)),
    ((231, 235), (44, 44)),
    ((237, 243), (46, 46)),
    ((256, 260), (49, 49)),
    ((262, 268), (51, 51)),
    ((281, 285), (54, 54)),
    ((287, 294), (56, 56)),
)
