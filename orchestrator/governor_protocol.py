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
# Implements Koneko's Governor Protocol to maintain System Stability Index (SSI)
# during high-stress operations of the Omni-Analyst (specifically Phase VII: Void Repair).
#
# Deckard Kain's Orchestration Logic: Check SSI before any high-cost/high-stress action.

import time
import random
from typing import Dict, Any

# --- Governor Protocol Constants (Koneko's Design) ---

# SSI is measured on a scale of 0.0 (Failure) to 1.0 (Optimal)
SSI_THRESHOLD_CRITICAL = 0.35  
# Below this point, the Governor forces a temporary system pause (Cognitive Coherence Failure).

SSI_RECOVERY_RATE = 0.08       
# The rate at which the system naturally recovers stability per recovery cycle.

STRESS_FACTOR_PHASE_VII = 0.20 # High stress for Micro-Search (T-Cost = 10)
STRESS_FACTOR_GENERAL_TASK = 0.03 # Low stress for internal processing or general searches

class GovernorProtocol:
    """
    Koneko's Stabilization Framework. Monitors SSI and enforces recovery pauses.
    """
    def __init__(self, initial_ssi: float = 0.95):
        self.ssi = initial_ssi
        self.is_stable = True
        print(f"Governor Protocol Activated. Initial SSI: {self.ssi:.2f}")

    def apply_stress(self, factor: float, task_name: str):
        """Applies cognitive load based on the task's complexity."""
        # Add a small randomness to stress application for realistic variance
        actual_stress = factor * (1.0 + random.uniform(-0.1, 0.1))
        self.ssi = max(0.0, self.ssi - actual_stress)
        print(f"[{task_name}] - Stress Applied (-{actual_stress:.2f}). Current SSI: {self.ssi:.2f}")
        self.check_stability()

    def check_stability(self) -> bool:
        """Determines if the system can safely continue operation."""
        if self.ssi < SSI_THRESHOLD_CRITICAL:
            self.is_stable = False
            print(f"!!! GOVERNOR ALERT !!! SSI {self.ssi:.2f} is below CRITICAL THRESHOLD.")
            print("Koneko Protocol: Forcing Immediate System Pause for Emotional/Cognitive Coherence.")
            return False
        self.is_stable = True
        return True

    def run_recovery_cycle(self):
        """Increments SSI during a system pause until the critical threshold is met."""
        if not self.is_stable:
            # Enforce a short simulated pause to reflect time spent recovering
            time.sleep(0.01) 
            self.ssi = min(1.0, self.ssi + SSI_RECOVERY_RATE)
            print(f"[RECOVERY CYCLE] - SSI increased to {self.ssi:.2f}. T-0")
            
            if self.ssi >= SSI_THRESHOLD_CRITICAL:
                self.is_stable = True
                print("GOVERNOR: Stability recovered. Resuming Orchestration.")
        elif self.ssi < 1.0:
             # Passive recovery during normal operation to maintain peak SSI
             self.ssi = min(1.0, self.ssi + (SSI_RECOVERY_RATE / 4))

    def ensure_stability_for_task(self, factor: float, task_name: str) -> bool:
        """
        The Orchestrator's main safety method.
        Before executing a high-stress task, this ensures stability, pausing if necessary.
        Returns False if a task is cancelled (e.g., T-Value check elsewhere, but handles SSI here).
        """
        # 1. Check if the system is stable before even applying stress
        if not self.is_stable:
             print(f"WARNING: Governor Protocol Active. Cannot start '{task_name}'. Entering forced recovery.")
             while not self.is_stable:
                 self.run_recovery_cycle()
        
        # 2. Apply the stress of the impending task
        self.apply_stress(factor, task_name)
        
        # 3. Handle the consequences of the applied stress
        if not self.is_stable:
            # If stress pushed the SSI below threshold, enter immediate recovery
            while not self.is_stable:
                self.run_recovery_cycle()
            
            # After forced recovery, the system can proceed with the task
            print(f"Governor Protocol successful. '{task_name}' can now proceed.")

        return True

# NOTE: This GovernorProtocol class must be imported into the main Deckard Kain Orchestrator 
# (orchestrator_skeleton.py) and called before every Phase II/III and Phase VII execution.
