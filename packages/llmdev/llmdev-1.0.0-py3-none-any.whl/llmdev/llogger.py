#!/usr/bin/env python

############################################
# Tools for LLM applications development   # 
# Copyright (c) 2024 IncubeAI              #
# Software released under the MIT license  #
# Visit https://github.com/incubeai/llmdev #
#                    for more information. #
############################################

import logging
import sys

def logOn():
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))