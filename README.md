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

Now to execute the attesteaion, the mes container (prover) and erp container (verifier) can be used as a example.

This are the possible commands that could be used:

- The prover can check if it has pending requests

```
docker exec -it mes bash
python3 attmgr.py checkRequest 073B
```

- The validator can query the blockchain to know the state of the prover

```
docker exec -it erp bash

python3 attmgr.py trustQuery 098d 073B
```

- The prover can submit evidence if there is a request pending

```
python3 attmgr.py  submitEvidence 073B 7A09AB47D4 688e115dcbe148cfadb12af421a028fab25e94586a6906fcfb4818172bedd49d7d07bb33722d179901534e2824ef64e43cd88b7fb4c11f93cf86258b05d0fb47

```

### Simulation

This simulation helps to compare the centralized from the decentralized implementation.

Now you can run the simulation like this

```
python3 simulator.py <simType> <simRepetitions> <simDuration> <rate>
```

This is the meaning of the parameters:

- **systemType*** : The system you want to simulate (centralized or decentralized)

- **simType**: The type of simulation (setup, run100 (iterations unit 100% hit rate), hitrate, maxquery)

- **simRepetitions**: Repetitions of the siumlation for run100.

- **sumDuration**: Maximum duration of each iteration of the simunlation.

- **rate**: defines the query rate.

For example:

```
python3 simulator.py centralized hitrate 1 1 5
```
 

