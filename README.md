# Energy Smart Grid Load Balancer

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/Graph_Theory-NetworkX-blue.svg)](https://networkx.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade Smart Grid simulation** for load balancing and fault tolerance. This repository uses Graph Theory (NetworkX) to model power distribution networks, simulate load spikes, and automatically reroute power to prevent substation failure.

## 🚀 Features

- **Grid Topology Modeling**: Represents Power Plants, Substations, and Consumers as a directed graph.
- **Load Flow Simulation**: Simulates electricity flow from generation to consumption.
- **Overload Detection**: Identifies transmission lines or substations exceeding capacity.
- **Auto-Balancing**: Basic algorithm to shed load or reroute flow (simulation).
- **Visualisation**: Exports grid topology properties.

## 📁 Project Structure

```
energy-smart-grid-load-balancer/
├── src/
│   ├── grid_graph.py     # Network Topology
│   ├── balancer.py       # Load Flow Logic
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/energy-smart-grid-load-balancer.git

# Install
pip install -r requirements.txt

# Run Load Balancer
python src/main.py
```

## 📄 License

MIT License
