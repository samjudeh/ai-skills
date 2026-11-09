APIM investigation checklist
Use only the sections relevant to the reported symptom.

Scope and timing
What is the UTC start and end time?
Is the issue limited to one API, operation, region, or instance?
Is it intermittent or reproducible?
Request path
Where was the error observed: client, APIM gateway, or backend?
Are there request IDs or correlation IDs that connect the observations?
What do available gateway and backend logs actually show?
Changes and dependencies
Were policies, certificates, DNS, networking, or backends changed?
Is a dependency failing independently of APIM?
Evidence standard
Quote or cite the log entry or source behind each confirmed finding.
Treat a missing log entry as an evidence gap, not proof that an event did not occur.
Label proposed explanations as hypotheses until validated.
