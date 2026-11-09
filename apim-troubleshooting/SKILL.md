name: apim-case-triage description: triage azure api management support cases using supplied symptoms and evidence. use when asked to organize an apim investigation, review request logs, or prepare an evidence-based case summary.
APIM case triage
Establish the reported symptom, affected API or operation, timeframe, and expected behavior. Ask for missing details only if they block analysis.
Read references/investigation-checklist.md and select only the checks relevant to this case.
If the user supplies a CSV with timestamp and status_code columns, run python scripts/summarize_statuses.py <csv-path> to calculate status-code counts. Do not run it on other file formats.
Separate:
Confirmed observations, with their source
Plausible hypotheses, labeled as hypotheses
Specific checks that would confirm or rule out each hypothesis
Do not infer root cause from status-code counts alone. Do not invent telemetry, customer impact, product behavior, or mitigation steps.
Return a concise summary with: symptom, confirmed evidence, open questions, next validation steps, and a customer-safe update if requested.
