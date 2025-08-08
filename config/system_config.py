import os
from dotenv import load_dotenv
load_dotenv()
MODEL = "gpt-4o-mini"
API_KEY = os.getenv("OPENAI_API_KEY")
TEXT_MENTION = "APPROVE"
MAX_TURNS = 15
MAX_TURNS_VOTING = 5
USER_PROXY_NAME = "UserProxy"
SAMPLE_TASK = """My email id is "mkumari233107@gmail.com" and my name is "USER1222"
The draft for the bill is:-
Data Privacy Regulation Act, 2025

Preamble

An Act to provide for the regulation, protection, and processing of personal data of individuals, and
to establish a Data Protection Authority for effective enforcement and grievance redressal.

Section 1 – Definitions

a) "Data Subject" means any individual whose personal data is being processed.
b) "Data Controller" refers to any individual or organization that determines the purposes and
means of processing personal data.
c) "Processing" includes any operation performed on personal data, such as collection, recording,
storage, adaptation, or alteration.

Section 2 – Rights of Data Subjects

Every data subject shall have the right to:
1. Access their personal data being processed.
2. Request correction of inaccurate or incomplete data.
3. Withdraw consent at any time.
4. Be informed of data breaches affecting their personal information.

Section 3 – Obligations of Data Controllers

1. Ensure that personal data is processed lawfully, fairly, and transparently.
2. Collect data only for specified, explicit, and legitimate purposes.
3. Maintain data accuracy and ensure it is up to date.
4. Implement technical and organizational measures to ensure data security.

Section 4 – Data Protection Authority

A Data Protection Authority (DPA) shall be established to oversee enforcement, conduct
investigations, and issue guidelines.
The DPA shall have powers to impose penalties, summon witnesses, and mandate data audits.

Section 5 – Penalties and Enforcement

Any violation of this Act shall attract monetary penalties up to n10 crores or 2% of annual turnover,
whichever is higher.
In cases of willful misconduct, criminal liability shall be pursued.

Section 6 – Amendments

The Parliament may amend any section of this Act by a simple majority vote with appropriate
justification and review.
Certification

This bill is proposed for review and debate by the legislative assembly. The provisions are subject
to judicial evaluation, political deliberation, and necessary amendment before passage."""