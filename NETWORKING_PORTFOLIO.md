# Computer Networks & Networked Systems Portfolio

This page is a focused entry point for my networking work. My primary portfolio direction remains **Embedded Systems and IoT**; this index collects the projects that are most relevant to computer networks, IoT networking, software-defined networking, protocol analysis, monitoring, and secure communications.

## Selected Projects

| Project | Main evidence |
| --- | --- |
| [Enterprise Network Design & Verification](https://github.com/amirhossein-sadeghi2003/network-lab-final-project) | VLANs, inter-VLAN routing, EtherChannel, DHCP/relay, RIP, multi-area OSPF, EIGRP, route redistribution, HSRP, NAT/PAT, ACLs, SSH, wireless connectivity, and representative end-to-end verification in Cisco Packet Tracer |
| [IoT Facility Network Monitoring](https://github.com/amirhossein-sadeghi2003/iot-facility-network-monitoring) | Segmented Admin/Staff/IoT/Guest/Services VLANs, inter-VLAN routing, DHCP, IoT registration, Syslog monitoring, SSH restrictions, and documented simulator limitations |
| [Cellular DTMF Control](https://github.com/amirhossein-sadeghi2003/cellular-dtmf-control) | STM32F407 + SIM800C system with SIM/network-registration checks, signal-strength queries, AT-command exchange, asynchronous UART parsing, incoming-call state handling, and repeated-call hardware validation |
| [IoT Digital Twin & ML Pipeline](https://github.com/amirhossein-sadeghi2003/IoT-DigitalTwin-ML-Pipeline) | ESP32 sensor telemetry, MQTT messaging, Python services, and Node-RED monitoring in a local IoT data pipeline |
| [Secure IoT Sensor Anomaly Detection](https://github.com/amirhossein-sadeghi2003/secure-iot-sensor-anomaly-detection) | Defensive monitoring of environmental telemetry with rule-based and ML detectors, including explicit cross-device generalization limitations |

## Protocol and SDN Coursework

The lower-level networking and SDN work is preserved in my undergraduate coursework archive. A curated index is available here:

- [Networking and SDN Coursework Index](https://github.com/amirhossein-sadeghi2003/undergraduate-coursework-archive/blob/main/NETWORKING_AND_SDN.md)

It links directly to work involving:

- Linux `PF_PACKET` raw sockets and Ethernet/ARP/IPv4 parsing;
- TCP socket and HTTP/Wireshark analysis;
- Mininet topologies;
- OpenFlow and Open vSwitch;
- explicit `ovs-ofctl` flow rules;
- `ping` and `iperf` connectivity/throughput checks;
- eight Network Laboratory sessions covering switching, routing, DHCP, SSH, security, OSPF, and redistribution.

## What This Track Demonstrates

- protocol-level work in C and Linux;
- routing and switching configuration and verification;
- SDN experimentation with Mininet/OpenFlow/Open vSwitch;
- IoT and cellular connectivity;
- network monitoring and segmentation;
- defensive security and access-control concepts;
- documentation of failed, partial, or simulator-limited results instead of presenting them as fully validated.

## Scope

Most enterprise-networking work here is implemented in Cisco Packet Tracer, while the protocol/SDN exercises use Linux networking tools, Mininet, OpenFlow, and Open vSwitch. The cellular and MQTT projects add real embedded/networked-system experience, but they are not presented as carrier-network or large-scale distributed-systems deployments.
