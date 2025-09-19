# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SurveyResponse(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.social.doctype.survey_answer.survey_answer import SurveyAnswer
		from frappe.types import DF

		answer: DF.Table[SurveyAnswer]
		respondant_email: DF.Data | None
		respondant_name: DF.Data | None
		survey: DF.Link | None
	# end: auto-generated types
	pass
