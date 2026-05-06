from orchestrator import OrchestratorAgent


def main():
    file_path = input("Enter internship application file path: ").strip().strip('"')

    orchestrator = OrchestratorAgent()
    result = orchestrator.run(file_path)

    print("\nFinal IDP Result:")
    print(result["idp_result"])

    print("\nFinal Student Notification:")
    print(result["student_notification"]["student_message"])


if __name__ == "__main__":
    main()