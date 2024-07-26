import pytest

from protozfits import File, recompress_zfits

test_file = "src/protozfits/tests/resources/example_LST_R1_10_evts.fits.fz"


def test_recompress_help():
    with pytest.raises(SystemExit) as e:
        recompress_zfits.main(["--help"])
    assert e.value.code == 0


def test_recompress(tmp_path):
    output_path = tmp_path / "recompressed.fits.fz"
    recompress_zfits.main([test_file, str(output_path), "--default-compression=zstd9"])
    assert len(File(str(output_path)).Events) == 10


def test_recompress_n_events(tmp_path):
    output_path = tmp_path / "recompressed.fits.fz"
    recompress_zfits.main(
        [test_file, str(output_path), "-n", "5", "--default-compression=zstd9"]
    )
    assert len(File(str(output_path)).Events) == 5
