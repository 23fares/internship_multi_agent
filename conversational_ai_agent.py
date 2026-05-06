class KnowledgeBasedConversationalAIAgent:
    def generate_message(self, idp_result):
        print("[Knowledge-Based Conversational AI Agent] Generating student message...")

        status = idp_result.get("status")
        missing_items = idp_result.get("missing_items", [])

        if status == "SUCCESS":
            message = (
                "Dear student, your internship application has been checked successfully. "
                "All required documents and signatures are complete. "
                "Your application will now move to the next stage."
            )

        elif status == "ERROR":
            formatted_missing_items = self._format_missing_items(missing_items)

            message = (
                "Dear student, your internship application is incomplete. "
                f"The following required item(s) are missing: {formatted_missing_items}. "
                "Please update your application and upload the missing information before resubmitting."
            )

        else:
            message = (
                "Dear student, your internship application could not be fully verified. "
                "Please contact the internship office or review your uploaded document."
            )

        return {
            "agent": "Knowledge-Based Conversational AI Agent",
            "input_received_from": "IDP Agent",
            "student_message": message,
            "next_step": "Notify Student",
            "reasoning_log": [
                "The IDP Agent result was received.",
                "The application status was checked.",
                "A clear student-facing notification message was generated."
            ]
        }

    def _format_missing_items(self, missing_items):
        if not missing_items:
            return "none"

        readable_items = []

        for item in missing_items:
            readable_items.append(item.replace("_", " "))

        return ", ".join(readable_items)