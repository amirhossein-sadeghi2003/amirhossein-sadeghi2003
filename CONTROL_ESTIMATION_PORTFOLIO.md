# Control, Estimation & Autonomous Systems Portfolio

This page is a focused entry point for my work in state estimation, sensor fusion, feedback control, navigation, and optimization. My primary portfolio direction remains **Embedded Systems and IoT**; this track extends that hardware/software background toward intelligent physical systems.

## Selected Projects

| Project | Main evidence |
| --- | --- |
| [Adaptive Mobile Navigation Fusion](https://github.com/amirhossein-sadeghi2003/adaptive-mobile-navigation-fusion) | Real phone GPS/IMU logs, 2D Kalman filtering, GPS dropout/jump experiments, innovation gating, IMU-heading dead reckoning, and an EKF with heading in the state |
| [Embedded IMU Attitude Estimation](https://github.com/amirhossein-sadeghi2003/embedded-imu-attitude-estimation) | ESP32 + MPU6050 hardware, startup gyro-bias calibration, complementary-filter roll/pitch estimation, ~50 Hz logging, Python analysis, OLED output, and physical testing |
| [Ball-and-Beam Hardware Control](https://github.com/amirhossein-sadeghi2003/ball-and-beam-hardware-control) | Physical ESP32/HC-SR04/MG946R prototype with initial P-based feedback control, partial stabilization, overshoot, and documented mechanical/sensing limitations |
| [Evolutionary Control Tuning](https://github.com/amirhossein-sadeghi2003/evolutionary-control-tuning) | Reproducible ball-and-beam simulation with PID control and a seeded genetic algorithm for controller tuning |
| [Sensor Fusion State Estimation](https://github.com/amirhossein-sadeghi2003/sensor-fusion-state-estimation) | Controlled 2D simulation with GPS-like measurements, IMU-like acceleration, Kalman filtering, GPS dropout, noise sweeps, and IMU-bias sensitivity |

## Representative Results

### Adaptive Mobile Navigation Fusion

Using a controlled injected GPS jump, innovation gating reduced maximum jump-window error from about **26.5 m to 3.8 m** relative to the unmodified phone-GPS path. During a simulated 15-second GPS outage, the EKF experiment reached about **10.9 m** maximum error against withheld phone GPS samples.

These are comparative experiments on one phone-collected walk; phone GPS is not surveyed ground truth.

### Evolutionary Control Tuning

In the documented seeded simulation, the GA-selected controller reduced mean absolute tracking error from **0.0618 m to 0.0363 m** and settling time from **2.96 s to 0.88 s** relative to the manual baseline.

The plant is deliberately simplified and the selected gains are not claimed to be globally optimal or hardware-validated.

### Ball-and-Beam Hardware Control

The physical prototype reached initial closed-loop P-based testing and could partially stabilize slow ball motion around the target. Faster motion produced overshoot and the string linkage limited repeatability. No quantitative closed-loop performance claim is made because no closed-loop telemetry log was retained.

## What This Track Demonstrates

- Kalman filtering and EKF-based state estimation;
- sensor fusion and navigation fault experiments;
- complementary filtering and gyro-bias calibration on real hardware;
- physical feedback-control bring-up;
- PID simulation and optimization;
- explicit separation between real-hardware results, simulated experiments, and incomplete work.

## Work Intentionally Not Featured as a Completed Result

[Learned Gyro Denoising](https://github.com/amirhossein-sadeghi2003/learned-gyro-denoising) currently establishes a reproducible raw-gyro baseline on EuRoC data, but the learned denoiser is not implemented yet. It is therefore not used here as evidence of a completed learned-estimation result.
