# Video-Based Exam Cheating Detection

## Description

A video surveillance system that automatically flags suspicious behaviour during written exams. A camera feed is processed in real time to detect anomalies — unusual head movements, out-of-seat activity, or irregular attention patterns — and logs potential cheating events for review.

## What it brings

Academic integrity systems today rely heavily on human invigilators. This project explores how computer vision can assist by handling the continuous monitoring task, flagging only the moments that warrant human attention — reducing fatigue and increasing consistency.

## How it works

The Python backend uses OpenCV to process the video stream frame by frame. Motion detection identifies activity zones, and behavioural filters isolate patterns that deviate from expected exam behaviour. A React frontend allows uploading recorded exam footage and browsing flagged timestamps. The architecture is modular, with audio analysis planned as a future extension.

## Status

🔄 Core detection functional — audio module in development.

## Tech Stack

`Python` · `OpenCV` · `React` · `Vite` · `JavaScript`
