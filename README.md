# Edencore Runtime

The Edencore Runtime is the embodiment layer of the Edencore system.  
It provides the execution environment where agents, minds, and governance interact.

## Structure

```
runtime/
    core/       # Runtime lifecycle and system manager
    bots/       # Bot class and orchestrator
    esm/        # Silicon mind loader and adapters
    mindcore/   # Governance interface
    api/        # External interface layer
```

## Purpose

The Runtime connects three major layers:

- **Mindcore** — governance, permissions, constitutions  
- **ESM** — silicon cognition and mind models  
- **Bots** — runtime agents that host minds  

This repository contains the foundational architecture for that system.

## Status

This is an early-stage skeleton.  
Functionality will expand as the Mindcore and ESM layers evolve.