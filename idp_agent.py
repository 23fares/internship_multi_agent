class IDPAgent:
    def __init__(self):
        self.required_items = {
            "student_name": ["student name", "name:"],
            "student_id": ["student id", "id:"],
            "department": ["department"],
            "cv": ["cv", "resume"],
            "internship_form": ["internship form"],
            "student_signature": ["student signature"]
        }

    def analyze_document(self, document_text):
        print("[IDP Agent] Analyzing uploaded internship document...")

        lower_text = document_text.lower()
        found_items = []
        missing_items = []

        for item, keywords in self.required_items.items():
            if any(keyword in lower_text for keyword in keywords):
                if self._has_value_after_keyword(lower_text, keywords):
                    found_items.append(item)
                else:
                    missing_items.append(item)
            else:
                missing_items.append(item)

        if missing_items:
            status = "ERROR"
            decision = "The internship application is incomplete."
        else:
            status = "SUCCESS"
            decision = "The internship application is complete."

        return {
            "agent": "IDP Agent",
            "status": status,
            "decision": decision,
            "found_items": found_items,
            "missing_items": missing_items,
            "next_agent": "Knowledge-Based Conversational AI Agent",
            "reasoning_log": [
                "The document text was extracted successfully.",
                "The required internship fields were checked.",
                "Missing fields were identified based on required document items."
            ]
        }

    def _has_value_after_keyword(self, text, keywords):
        lines = text.splitlines()

        for line in lines:
            line = line.strip()

            for keyword in keywords:
                if keyword in line:
                    parts = line.split(":", 1)

                    if len(parts) == 2 and parts[1].strip():
                        return True

                    if len(parts) == 1:
                        return True

        return False