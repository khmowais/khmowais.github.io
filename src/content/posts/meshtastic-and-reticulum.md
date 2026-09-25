---
title: "Meshtastic and Reticulum: Building the Network the Cell Companies Won't"
description: LoRa meshes and long-range packet autonomy — what they are, what they're for, and the honest throughput math.
pubDate: '2026-08-02'
tags:
- Radio
- Emergency Comms
- Local First
author: Khawaja M. Owais
audience: personal
readingMinutes: 6
sources:
- https://meshtastic.org/docs/
- https://reticulum.network/
- https://github.com/markqvist/Reticulum
---

Cell networks are an argument with geography: where the tower is, the network is. The off-grid radio movement runs on a different premise — the network is carried by the people who use it, and it exists wherever *somebody* turns on a radio. Two projects carry this banner with notably different styles.

## Meshtastic: LoRa as a mesh you hold in your hand

Meshtastic builds a mesh network out of LoRa radios — the long-range, low-throughput radio technology famously used for IoT sensors with AA-battery lifetimes. Its genius is the deployment model: cheap boards (ESP32-class microcontrollers with a radio module), open firmware, and zero infrastructure. Every node relays for every other node, so coverage grows as people join, like a geocache network made of packets.

What it is actually for, honestly:

- **Off-grid messaging.** Firmware-level text messages and broadcasts between meshed peers, no base station.
- **Position and telemetry.** Nods to GPS and sensor feeds relayed across the mesh.
- **The comfort that doesn't need a bill** — when the fiber goes down and the cell towers go quiet, the mesh does not notice, because the mesh *is* the users.

The honest math to keep in your head: LoRa throughput is tiny. This is not your web browser. Measure it in kilometers per hop and bytes per minute — it is a *pulse check* network, a bubble of presence and gossip, not a file delivery service. That is not a flaw; it is the spec. Know it, and you will not be disappointed that the node did not fetch your email.

## Reticulum: packet radio, grown up and independent

Reticulum is a different animal: a networking *stack*, not a single app. It treats radio, and an internet connection when available, as interchangeable transport for a self-contained packet network designed to keep operating without any central infrastructure. It powers chat, file transfer, location services and more over whatever links exist — LoRa, the ax.25 packet world, TCP — and it is built on the premise that the network is not a handheld gadget but a *protocol*.

Where Meshtastic is a product you run, Reticulum is a layer you build on. The project's own documentation is worth the download for the thread of context around encrypted, autonomous networks — and the source is open, which for this shelf is not a detail but the *point*.

## The shared hypothesis

Both projects are running the same quiet experiment: **if the network is owned by its operators, nobody can turn it off.** That is a resilience property that applies to the infrastructure you depend on for safety, and it is the same philosophy that runs through the local-first movement — own your data, run your own node, keep the copy where you can see it. The radio shelf and the ownership shelf are the same shelf from two directions.

## What to do about it

Get a node, or build one — the Meshtastic docs are thorough and the boards cost less than a dinner. Run it at an event, on a hike, through a power cut. Deliver a message across a field with no tower in sight and the abstraction collapses into a fact you can feel: the network is not out there. It is in your hand, and it works because you turned it on.