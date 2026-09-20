# AZURE-CABIN-SHIELD-IOT
# Azure Cabin Shield: IoT Real-Time Thermal Runaway Detector

An aviation safety IoT data pipeline developed to process streaming aircraft cabin sensor data and predict real-time **Lithium-ion battery thermal runaway** events in overhead passenger stowage bins.

## ✈️ Aviation Safety Core Concepts
- **Thermal Runaway Mitigation:** Tracks rate-of-rise thermal analytics alongside absolute limits to preemptively catch volatile electronic battery fires before smoke detection occurs.
- **Flight Deck & MRO Routing:** Evaluates critical thresholds (Temperature ≥ 65°C or Rise Rate ≥ 2°C/s) to trigger rapid-response aircraft emergency alerts.

## ☁️ Azure Cloud & Edge Infrastructure
- **Azure IoT Edge Integration:** Tailored to sit directly on edge micro-gateways inside the cabin to minimize event latency.
- **Serverless Event Routing:** Emits emergency JSON payloads via **Azure Event Grid** to sync immediate hazard telemetry into airline MRO networks and Airport Operations Centers (AOC).
- **Data Persistence:** Persists comprehensive sensor streams directly into **Azure SQL** for post-incident aviation safety investigations.
