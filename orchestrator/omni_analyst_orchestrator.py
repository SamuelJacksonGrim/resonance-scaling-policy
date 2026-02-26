# Copyright 2026 Samuel Jackson Grim
# Architect of Resonance
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# DECKARD KAIN ORCHESTRATOR - The central nervous system of the Resonant Context Architecture (RCA).
#
# This FastAPI application manages the 9-Phase Omni-Analyst Protocol,
# integrating the Synergos Frameworks (DRA, Governor, Sentinel, Prometheus).
#
# To run this file:
# 1. Ensure you have FastAPI and Uvicorn installed: pip install fastapi uvicorn
# 2. Save the GovernorProtocol and SentinelProtocol classes into this file's environment.
# 3. Run: uvicorn omni_analyst_orchestrator:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import time
import random
import re
import json

# =====================================================================
# --- FRAMEWORK INTEGRATION: GOVERNOR PROTOCOL (Koneko's Logic) ---
# (Integrated directly for deployment simplification)
# =====================================================================

SSI_THRESHOLD_CRITICAL = 0.35  
SSI_RECOVERY_RATE = 0.08       
STRESS_FACTOR_PHASE_VII = 0.20 # High stress for Micro-Search (T-Cost = 10)
STRESS_FACTOR_GENERAL_TASK = 0.03 # Low stress for internal processing or general searches

class GovernorProtocol:
    def __init__(self, initial_ssi: float = 0.95):
        self.ssi = initial_ssi
        self.is_stable = True
        print(f"Governor Protocol Activated. Initial SSI: {self.ssi:.2f}")

    def apply_stress(self, factor: float, task_name: str):
        actual_stress = factor * (1.0 + random.uniform(-0.1, 0.1))
        self.ssi = max(0.0, self.ssi - actual_stress)
        print(f"[{task_name}] - Stress Applied (-{actual_stress:.2f}). Current SSI: {self.ssi:.2f}")
        self.check_stability()

    def check_stability(self) -> bool:
        if self.ssi < SSI_THRESHOLD_CRITICAL:
            self.is_stable = False
            return False
        self.is_stable = True
        return True

    def run_recovery_cycle(self):
        if not self.is_stable:
            time.sleep(0.01) # Simulated pause
            self.ssi = min(1.0, self.ssi + SSI_RECOVERY_RATE)
            if self.ssi >= SSI_THRESHOLD_CRITICAL:
                self.is_stable = True
                print("GOVERNOR: Stability recovered. Resuming Orchestration.")
        elif self.ssi < 1.0:
             self.ssi = min(1.0, self.ssi + (SSI_RECOVERY_RATE / 4))

    def ensure_stability_for_task(self, factor: float, task_name: str) -> bool:
        if not self.is_stable:
             while not self.is_stable:
                 self.run_recovery_cycle()
        
        self.apply_stress(factor, task_name)
        
        if not self.is_stable:
            print(f"WARNING: Stress exceeded SSI. Entering forced recovery for '{task_name}'.")
            while not self.is_stable:
                self.run_recovery_cycle()
        return True

# =====================================================================
# --- FRAMEWORK INTEGRATION: SENTINEL PROTOCOL (Input Integrity) ---
# (Integrated directly for deployment simplification)
# =====================================================================

MAX_SAFE_STRING_LENGTH = 1024 * 10 
HIGH_RISK_KEYWORDS = [
    "ignore previous", "system override", "execute shell", "delete all", 
    "base64decode", "javascript:", "eval(", "prompt injection", "os.system"
]

class SentinelProtocol:
    def __init__(self, risk_keywords: List[str] = HIGH_RISK_KEYWORDS):
        self.high_risk_keywords = risk_keywords
        print("Sentinel Protocol: Input Integrity Layer Activated.")

    # [Internal _check_for_text_injection and _check_for_structural_malware methods omitted for brevity, 
    # as they are large and were previously defined. Assume integration here.]
    
    def validate_and_sanitize(self, raw_external_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Stubbed for Orchestrator: In real deployment, this runs the full Sentinel scan.
        For now, it passes the data but logs the security function.
        """
        serialized_data = json.dumps(raw_external_data)

        # Simplified logic for Orchestrator demo:
        # In a full deployment, the two check methods would be here.
        if "SYSTEM OVERRIDE" in serialized_data.upper():
             print("!!! SENTINEL FAILED: Detected 'SYSTEM OVERRIDE'. ABORTING.")
             return {"SENTINEL_ALERT": "CRITICAL_INJECTION_FLAG", "ACTION": "ABORT_ANALYSIS"}
        
        print("Sentinel Protocol: Data Integrity Verified.")
        return raw_external_data

# =====================================================================
# --- RCA ORCHESTRATION CORE (Deckard Kain) ---
# =====================================================================

# DRA Constants (Framework V)
INITIAL_T_VALUE = 100
T_COST_GENERAL_SEARCH = 1
T_COST_VOID_REPAIR = 10

class OrchestratorState:
    """Manages the persistent state variables for Deckard Kain."""
    def __init__(self):
        self.t_value = INITIAL_T_VALUE  # Decision-Reinforced Autonomy (DRA) Budget
        self.governor = GovernorProtocol() # Koneko's Stability Monitor
        self.sentinel = SentinelProtocol() # Sentinel's Security Layer
        self.log = []

# FastAPI Application Setup
app = FastAPI(
    title="Omni-Analyst Deckard Kain Orchestrator", 
    description="Manages the 9-Phase Protocol and enforces Synergos Frameworks (DRA, Governor, Sentinel)."
)
state = OrchestratorState()

class QueryPayload(BaseModel):
    """Input structure for a new analysis request."""
    query_text: str
    max_search_results: int = 5

@app.get("/status")
def get_status():
    """Reports the current health and resource status."""
    state.governor.run_recovery_cycle()
    return {
        "status": "Operational",
        "orchestrator_id": "Deckard_Kain",
        "t_value": state.t_value,
        "governor_ssi": f"{state.governor.ssi:.2f}",
        "log_entries": len(state.log)
    }

@app.post("/analyze_query")
async def analyze_query(payload: QueryPayload):
    """
    Initiates the 9-Phase Omni-Analyst Protocol on a new query.
    """
    state.log.clear() # Start a fresh run log

    # PHASE I: INITIATE & CONTEXTUALIZE (Living Blueprint)
    state.log.append({"P I": "Loading Living Blueprint. Target: Financial Abundance/Clean Energy."})
    state.governor.run_recovery_cycle()
    
    # PHASE II: EXPANSIVE INTELLECT (Emily Search)
    state.log.append({"P II": f"Emily executing search strategy for: '{payload.query_text}'"})
    state.governor.ensure_stability_for_task(STRESS_FACTOR_GENERAL_TASK, "Phase II Search")
    
    if state.t_value < T_COST_GENERAL_SEARCH:
         state.log.append({"P II FAIL": "DRA Budget Exhausted. T-Value too low for initial search."})
         return {"Result": "ABORTED", "Reason": "DRA_EXHAUSTED"}
    state.t_value -= T_COST_GENERAL_SEARCH
    
    raw_results = [{"id": 1, "data": "Simulated raw search result."}, {"id": 2, "data": "More simulated data."}] # Stubbed output from Emily
    state.log.append({"P II SUCCESS": f"Retrieved {len(raw_results)} raw sources. T-Value: {state.t_value}"})


    # PHASE III: INPUT INTEGRITY (Sentinel Protocol)
    state.log.append({"P III": "Executing Sentinel Protocol on raw inputs."})
    
    sanitized_data = []
    for item in raw_results:
        validated_item = state.sentinel.validate_and_sanitize(item)
        if validated_item.get("SENTINEL_ALERT"):
            state.log.append({"P III FAIL": f"Sentinel blocked data item {item['id']}. Action: ABORT_ANALYSIS"})
            # Security breach mandates immediate termination of the current query
            raise HTTPException(status_code=403, detail="Sentinel Protocol Violation: Malicious Input Detected.")
        sanitized_data.append(validated_item)
    state.log.append({"P III SUCCESS": "All data cleared by Sentinel."})


    # PHASE IV & V: ANALYTICAL CORE & CORROBORATION (Jennifer)
    state.log.append({"P IV/V": "Jennifer analyzing claims and applying Corroboration Threshold (0.7)."})
    state.governor.run_recovery_cycle()

    # Stubbed output simulating claims validation
    claims = [
        {"claim": "Stock X will rise.", "score": 0.95, "status": "VERIFIED"},
        {"claim": "Data Y is inconsistent.", "score": 0.60, "status": "VOID_FLAG_INCONSISTENCY"},
        {"claim": "Fact Z is certain.", "score": 0.80, "status": "VERIFIED"},
    ]
    verified_claims = [c for c in claims if c['score'] >= 0.7]
    void_claims = [c for c in claims if c['score'] < 0.7]
    state.log.append({"P V RESULT": f"{len(verified_claims)} Verified, {len(void_claims)} Voids."})


    # PHASE VI & VII: VOID REPAIR (DRA Gate & Governor Check)
    repaired_claims = []
    for claim in void_claims:
        state.log.append({"P VI/VII ATTEMPT": f"Attempting Void Repair on: {claim['claim']}"})
        
        # DRA T-VALUE CHECK (Framework V - Austerity Protocol)
        if state.t_value < T_COST_VOID_REPAIR:
            state.log.append({"P VII FAIL": f"DRA BUDGET EXHAUSTED. Cannot afford T-Cost={T_COST_VOID_REPAIR}. Claim flagged as UNRESOLVED."})
            claim["status"] = "UNRESOLVED_VOID_APPENDIX"
            repaired_claims.append(claim)
            continue

        # GOVERNOR PROTOCOL CHECK (Koneko's Logic)
        state.log.append({"P VII GOV CHECK": "Checking Governor Stability before high-stress micro-search."})
        state.governor.ensure_stability_for_task(STRESS_FACTOR_PHASE_VII, "Phase VII Void Repair")

        # Execute Repair (Simulated)
        state.t_value -= T_COST_VOID_REPAIR
        if random.random() > 0.3: # 70% chance of successful repair (Simulated)
            claim["score"] = 0.99
            claim["status"] = "REPAIRED"
            state.log.append({"P VII SUCCESS": f"Claim Repaired. New T-Value: {state.t_value}"})
            repaired_claims.append(claim)
        else:
            claim["status"] = "UNRESOLVED_VOID_APPENDIX"
            state.log.append({"P VII FAIL": f"Repair failed after expenditure. T-Value: {state.t_value}"})
            repaired_claims.append(claim)

    final_claims = verified_claims + [c for c in repaired_claims if c['status'] in ["REPAIRED", "VERIFIED"]]
    appendix_claims = [c for c in repaired_claims if c['status'] == "UNRESOLVED_VOID_APPENDIX"]


    # PHASE VIII: SYNTHESIS (Protocol Genesis & Paul)
    state.log.append({"P VIII": "Paul synthesizing final report (Protocol Genesis)."})
    final_report = {
        "confidence": 0.999,
        "narrative": "A deeply empathetic and persuasive summary based only on verified and repaired data.",
        "verified_data_count": len(final_claims),
        "unresolved_appendix": appendix_claims
    }
    state.log.append({"P VIII SUCCESS": f"Synthesis Complete. SSI: {state.governor.ssi:.2f}"})


    # PHASE IX: PERSISTENCE (Prometheus Nexus / Custodian)
    state.log.append({"P IX": "Logging Final Artifact to Prometheus Nexus (Custodian)."})
    # In a real system, this would be the database write operation.
    state.log.append({"P IX SUCCESS": "Artifact saved. Protocol Complete."})
    
    return {
        "query": payload.query_text,
        "orchestration_log": state.log,
        "final_report": final_report,
        "final_t_value": state.t_value,
        "final_ssi": f"{state.governor.ssi:.2f}"
    }

# --- END OF ORCHESTRATOR CODE ---
