# Kempower EV Charging Infrastructure & Grid Analytics

A data science and electrical grid simulation framework analyzing vehicle fleet distributions, infrastructure bottlenecks, and high-power grid telemetry across 9 European national corridors. This project processes a raw Kempower dataset containing over 71 Million transaction rows.

---

## Project Scope & Objectives

This project analyzes the Kempower dataset to optimize network performance, track grid loading, and output data-driven hardware deployment roadmaps. The analysis is divided into 4 core components:
1. Data Overview by Country: Mapping total network traffic logs.
2. Geographic Fleet Distribution: Profiling the top 5 most frequent EV models per country node.
3. Infrastructure Decision Matrix: Calculating real-world grid bottleneck threat scores by integrating external market metrics.
4. Empirical Grid Telemetry & Power Infrastructure Load Analysis: Evaluating continuous voltage, current draw, and power consumption spikes.

---

## Repository File Structure

* Country Filtering.py
  Uses a memory-safe data streaming pipeline (chunksize) to isolate and clean raw telemetry logs for our 9 target European national corridors.
* Top 5 Car model.py
  Aggregates the transaction dataset by country and car type to isolate localized vehicle fleet frequencies.
* Decision Matrix.py
  Blends the internal session counts with external market data using normalization formulas to compute real-world grid bottleneck threat scores.
* Grid Analysis.py
  Processes physical metrics over time using the 10-second increment samples to track average power delivery rates, peak transformer shocks, and total energy footprint.
* Kempower-EV-Charging-Infrastructure-Analysis.pdf
  The finalized executive presentation slide deck summarizing project outcomes and visualization charts.

---

## Dataset Schema & Architecture

The analytical pipeline evaluates localized grid behaviors by processing the following telemetry fields directly from the Kempower datasheet:
* transactionId / country / EVModel: Core session metadata.
* year / month / quarter / weekday: Temporal logging components.
* soc (State of Charge) / tempC: Battery physics and environmental attributes.
* sampleTime10sIncrement: Time-series trackers logged in continuous 10-second intervals.
* avgPowerW / avgCurrentA / avgVoltageV: Live electrical grid interaction parameters.

---

## External Data Integration

To build a predictive framework, internal infrastructure utilization counts were combined with macro vehicle statistics sourced from Open EV Charts (https://open-ev-charts.org/):
* 2025/2026 EV Market Share Percentages were used as a weight factor against historical data. This integration prevents the model from ignoring low-volume corridors that are experiencing massive, sudden EV adoption velocity.

---

## Empirical Telemetry Performance Matrix

Our processing pipeline generated the following technical profile across our active infrastructure network nodes:

| Country Node | Average Delivery (kW) | Peak Load Spike (kW) | Total Energy (MWh) | Infrastructure Strain Score | Strategic Recommendation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Denmark | 48.91 kW | 241.24 kW | 6.72 MWh | 7.0 / 10 | Critical Alert: Expand Stalls |
| Norway | 56.39 kW | 364.81 kW | 3,435.61 MWh | 6.6 / 10 | Critical Alert: Expand Capacity |
| Sweden | 62.79 kW | 365.54 kW | 753.87 MWh | 5.6 / 10 | High Priority: Upgrade Substation |
| Finland | 62.25 kW | 397.87 kW | 3,576.22 MWh | 5.3 / 10 | High Priority: Upgrade Substation |
| France | 53.18 kW | 253.20 kW | 510.69 MWh | 4.1 / 10 | Stable: General Traffic Monitoring |
| United Kingdom | 55.76 kW | 278.53 kW | 3,221.48 MWh | 4.8 / 10 | Stable: Balanced Asset Allocation |
| Portugal | 60.40 kW | 163.85 kW | 164.98 MWh | 3.9 / 10 | Monitor: Commercial Fleet Geometry |
| Latvia | 58.19 kW | 236.03 kW | 4.79 MWh | 1.4 / 10 | Stable: General Traffic Monitoring |
| Belgium | 42.88 kW | 90.47 kW | 34.42 MWh | 3.3 / 10 | Monitor: Commercial Fleet Geometry |

---

## Strategic Recommendations & Key Takeaways

1. Proactive Capital Allocation (Denmark Bottleneck)
   Do not rely solely on historical session volume to direct budget choices. While Denmark represents a low absolute volume node (49,457 sessions), its 71% EV market penetration triggers a critical 7.0 Strain Score. Station footprints here must be expanded proactively before the network experiences utilization failure.

2. Substation Electrical Hardening (Finland & Sweden)
   Telemetry isolated severe peak load spikes reaching 397.87 kW in Finland. To prevent transformer insulation breakdown and fuse failures from luxury EV battery cooling shocks, charging hubs along these corridors must be paired with dedicated 400 kVA to 500 kVA rated substations.

3. Physical Hub Layout Re-Engineering (Belgium & Portugal)
   Fleet distribution analysis uncovered a distinct structural shift in logistics corridors: the Maxus eDeliver 9 commercial utility van unexpectedly took the #1 spot in Belgium and Portugal. Kempower must deploy wide, pull-through commercial lanes at these sites rather than tight passenger car parking stalls to accommodate freight geometries.

---

## Environment Setup & Dependencies

Ensure your data environment has the core data science libraries installed before execution:
```bash
pip install pandas numpy
