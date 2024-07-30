from simpleexperimenttracker.simpleexperimenttracker import SimpleExperimentTracker


def test_simpleexperimenttracker():
    tracker = SimpleExperimentTracker()
    assert isinstance(tracker, SimpleExperimentTracker)
    assert tracker.experiment_name is None
    assert tracker.job_name is None


def test_simpleexperimenttracker_set():
    tracker = SimpleExperimentTracker(root_dir="tests/sandbox")
    tracker.set_experiment()
    tracker.set_job()
    assert isinstance(tracker, SimpleExperimentTracker)
    assert isinstance(tracker.experiment_name, str)
    assert isinstance(tracker.job_name, str)
    assert len(tracker.job_name) == 24


def test_simpleexperimenttracker_set_names():
    tracker = SimpleExperimentTracker(root_dir="tests/sandbox")
    tracker.set_experiment("exp")
    tracker.set_job("job")
    assert isinstance(tracker, SimpleExperimentTracker)
    assert isinstance(tracker.experiment_name, str)
    assert tracker.experiment_name == "exp"
    assert isinstance(tracker.job_name, str)
    assert tracker.job_name == "job"
