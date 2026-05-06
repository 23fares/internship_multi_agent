import os
import json
from document_loader import load_document_text
from idp_agent import IDPAgent
from conversational_ai_agent import KnowledgeBasedConversationalAIAgent


class OrchestratorAgent:
    def __init__(self):
        self.idp_agent = IDPAgent()
        self.chat_agent = KnowledgeBasedConversationalAIAgent()

    def run(self, file_path):
        print("[Orchestrator] Internship application file received.")
        print("[Orchestrator] Sending file to Document Loader...")

        document_text = load_document_text(file_path)

        project_path = os.path.join("projects", "Internship_Application_System")
        os.makedirs(project_path, exist_ok=True)

        extracted_text_path = os.path.join(project_path, "extracted_document_text.txt")
        with open(extracted_text_path, "w", encoding="utf-8") as file:
            file.write(document_text)

        print("[Orchestrator] Extracted text saved.")
        print("[Orchestrator] Sending extracted text to IDP Agent...")

        idp_result = self.idp_agent.analyze_document(document_text)

        idp_result_path = os.path.join(project_path, "idp_result.json")
        with open(idp_result_path, "w", encoding="utf-8") as file:
            json.dump(idp_result, file, indent=4)

        print("[Orchestrator] IDP Agent returned the result.")
        print("[Orchestrator] Sending IDP result to Knowledge-Based Conversational AI Agent...")

        chat_result = self.chat_agent.generate_message(idp_result)

        chat_result_path = os.path.join(project_path, "student_notification.json")
        with open(chat_result_path, "w", encoding="utf-8") as file:
            json.dump(chat_result, file, indent=4)

        log_path = os.path.join(project_path, "workflow_log.txt")
        with open(log_path, "w", encoding="utf-8") as file:
            file.write("[Orchestrator] Internship application file received.\n")
            file.write("[Orchestrator] File sent to Document Loader.\n")
            file.write("[Document Loader] Text extracted from uploaded document.\n")
            file.write("[Orchestrator] Extracted text sent to IDP Agent.\n")
            file.write("[IDP Agent] Document validation result returned.\n")
            file.write("[Orchestrator] IDP result sent to Knowledge-Based Conversational AI Agent.\n")
            file.write("[Knowledge-Based Conversational AI Agent] Student notification generated.\n")

        print("[Orchestrator] Student notification generated.")
        print("[Orchestrator] Results saved.")

        return {
            "idp_result": idp_result,
            "student_notification": chat_result
        }