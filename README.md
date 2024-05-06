# Blochain Based Remote Attestation

In this repository you will find the code implemented for a remote attestation that communicates devices via blockchain.

### Blockchain

The blockchain infrastructure is located in the Blockchain/ folder, to use the blockchain use the following commands.

To execute the docker containers needed run the following docker compose command.

```
docker-compose -f test.yml up
```

After this, to configure the system and upload the configuration to Sawtooth, the following command should be executed to begin the administrator container and load the admin client information.

```
docker exec -it administration-client bash

python3 administration.py loadSystemConfig ¬¬ python3 administration.py loadDeviceDB
```

Now to execute the attesteaion, the mes container should run, use the following commands as an example.

```
docker exec -it mes bash
python3 attmgr.py checkRequest 073B
```

### Simulation

First install the requierements for running the simulation

```
pip3 install -r requirements.txt
```

Now you can run the simulation like this

```
python3 simulator.py <simType> <simRepetitions> <simDuration> <rate>
```

This is the meaning of the parameters:

-	***systemType*** :  	  The system you want to simulate (centralized or decentralized)
- **simType**: The type of simulation (setup, run100 (iterations unit 100% hit rate), hitrate, maxquery)

- **simRepetitions**: Repetitions of the siumlation for run100 . The maximum should be defined here.

- **sumDuration**: Maximum duration of each iteration of the simunlation.

- **rate**: defines the query rate.

For example:

```
python3 simulator.py centralized hitrate 1 1 5
```
 

