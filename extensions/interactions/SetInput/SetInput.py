# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from extensions.interactions import base


class SetInput(base.BaseInteraction):
    """Interaction for input of an unordered set of strings."""

    name = 'Set Input'
    description = 'Allows learners to enter an unordered set of strings.'
    display_mode = base.DISPLAY_MODE_SUPPLEMENTAL
    _dependency_ids = []
    _handlers = [{
        'name': 'submit', 'obj_type': 'SetOfUnicodeString'}]

    # NB: There used to be a UnicodeString-typed parameter here called
    # 'element_type'. This has since been removed.
    _customization_arg_specs = []

    _answer_visualization_specs = [{
        # Table with answer counts.
        # TODO(msl): add option 'title': 'All answers'
        'id': 'TwoColumnFrequencyTable',
        'options': {
            'column_headers': ['Answer', 'Count']
        },
        'calculation_id': 'AnswerCounts',
    }, {
        # Table with answer counts for top N answers.
        # TODO(msl): add option 'title': 'Top 5 answers'
        'id': 'TwoColumnFrequencyTable',
        'options': {
            'column_headers': ['Answer', 'Count']
        },
        'calculation_id': 'Top5AnswerCounts',
    }, {
        # Table with most commonly submitted elements of set.
        # TODO(msl): add option 'title': 'Commonly submitted elements'
        'id': 'TwoColumnFrequencyTable',
        'options': {
            'column_headers': ['Element', 'Count']
        },
        'calculation_id': 'FrequencyCommonlySubmittedElements',
    }]
