# Module 01: Laboratory Exercises & Calibration Matrix

---

## 🎯 Objective
Empirically observe and map the phase transitions of token generation by systematically varying Temperature, Top-K, and Top-P across a single frozen creative prompt.

---

## ✍️ Step 1: Select Your Creative Writing Prompt Track

Choose **one** track below and freeze it. Do not change a single character of your prompt across all 7 runs.

### Track A: Speculative Hard Sci-Fi / Cyberpunk Narrative
> *"System Prompt: You are an avant-garde science fiction writer specializing in high-density technical worldbuilding and atmospheric cyberpunk prose.*  
> *Prompt: Describe the catastrophic decompression of an orbital data-vault above Low Earth Orbit, detailing the physical dispersion of optical quantum storage arrays, the silent vacuum, and the terminal telemetry log of the resident synthetic custodian."*

### Track B: Victorian Gothic Horror / Eldritch Atmosphere
> *"System Prompt: You are a 19th-century gothic novelist steeped in cosmic dread and psychological horror.*  
> *Prompt: The antiquarian unseals a lead-lined reliquary discovered beneath the foundations of an abandoned Benedictine priory, documenting the anomalous smell, the distortion of candlelight, and the realization that the relic is breathing."*

### Track C: Hardboiled Technical Post-Mortem / Incident Mystery
> *"System Prompt: You are a cynical, hardboiled distributed systems investigator writing a narrative incident report.*  
> *Prompt: It was 03:14 UTC when the distributed consensus cluster in Frankfurt dropped dead. Narrate the post-mortem like a classic noir crime investigation: the stale coffee, the smoking server racks, the split-brain state, and the rogue cron job that left no fingerprints."*

### Track D: Mythological Epic / Mythopoetic Worldbuilding
> *"System Prompt: You are an ancient chronicler reciting a lost cosmogonic epic.*  
> *Prompt: Recount the forging of the Celestial Meridian by the architect-titans, describing how molten star-iron was hammered against the anvil of the void to divide the day from the infinite dark."*

### Track E: Satirical Bureaucratic Dystopia / Absurdist Corporate Fiction
> *"System Prompt: You are an executive compliance officer in an absurdist, hyper-bureaucratic dystopia.*  
> *Prompt: Issue an urgent company-wide memorandum regarding the proper protocol for submitting Form 88-B ('Request for Voluntary Existence Re-Verification') following the sudden, unannounced cessation of linear time."*

---

## 🧪 Step 2: The 7-Run Calibration Matrix

Execute all 7 runs sequentially with your frozen prompt and log every metric:

| Run ID | Name | Temperature ($T$) | Top-K | Top-P | Target Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Run 1** | Deterministic Anchor | `0.0` | `1` | `1.0` | Maximum rigidity; greedy decoding; assess loop vulnerabilities. |
| **Run 2** | Low-Entropy Coherence | `0.2` | `40` | `0.8` | Conservative, safe lexical choices; high syntactic consistency. |
| **Run 3** | Balanced Standard | `0.7` | `40` | `0.9` | Baseline production standard; natural cadence and metaphor. |
| **Run 4** | High Temp / Constrained Nucleus | `1.2` | `40` | `0.5` | Can aggressive Top-P truncation rein in extreme thermal entropy? |
| **Run 5** | High Nucleus / Constrained Top-K | `0.9` | `10` | `0.95` | Does strict Top-K starve vocabulary before Top-P can act? |
| **Run 6** | High Entropy Exploration | `1.4` | `100` | `0.98` | Onset of semantic drift, surrealism, and novel vocabulary. |
| **Run 7** | Degeneration Stress Test | `1.8 - 2.0` | `200+` | `1.0` | Complete breakdown: phonetic loop, syntax collapse, unicode artifacting. |

---

## 📝 Step 3: Submission

Submit your results via the [Module 01 Submission Issue Form](https://github.com/Skillodev/sdl-lab-dev/issues/new?template=module-01-submission.yml).
