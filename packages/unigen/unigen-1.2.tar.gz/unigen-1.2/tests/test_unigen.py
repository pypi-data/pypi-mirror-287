import os
import shutil
import string
import random
from typing import Any, Callable, Optional, get_args
import unittest

from unigen import AudioFactory, IAudioManager, pictureTypes

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
baseFolder = os.path.join(__location__, "testSamples", "baseSamples")
modifiedFolder = os.path.join(__location__, "testSamples", "modifiedSamples")
coversPath = os.path.join(baseFolder, "covers")
covers = [os.path.join(coversPath, coverName) for coverName in os.listdir(coversPath)]

# Unicode range for common Japanese characters (Hiragana, Katakana, and common Kanji)
japanese_chars = [
    (0x3041, 0x3096),  # Hiragana
    (0x30A1, 0x30F6),  # Katakana
    (0x4E00, 0x9FBF),  # Common Kanji
]
all_japanese_chars = "".join(chr(x) for x in [k for start, end in japanese_chars for k in range(start, end)])
audioImpl: IAudioManager
filePathImpl: str


def getRandomCoverImageData() -> bytes:
    num_covers = len(covers)
    cover_index = random.randrange(0, num_covers, 1)
    path = covers[cover_index]
    # del covers[cover_index]
    with open(path, "rb") as image_file:
        image_data = image_file.read()
    return image_data


def generate_random_string(x: int, y: int):
    siz = random.randint(x, y)
    characters = string.ascii_letters + string.digits  # You can customize this further
    random_string = "".join(random.choice(characters) for _ in range(siz))
    return random_string


def generate_random_japanese_string(x: int, y: int) -> str:
    siz = random.randint(x, y)
    random_string = "".join(random.choice(all_japanese_chars) for _ in range(siz))
    return random_string


def select_random_keys_from_list(arr: list[Any]) -> list[Any]:
    num_keys_to_select = random.randint(2, len(arr))
    return random.sample(arr, num_keys_to_select)


class TestMutagenWrapper(unittest.TestCase):
    def setUp(self):
        self.audio = audioImpl
        self.file_path = filePathImpl
        self.single_cover_test = False  # for optimization, this will only test for one cover embed, hence greatly reducing test run time

    def test_title(self):
        test_arr = ["title1", "title2", "title3", generate_random_string(5, 20), generate_random_japanese_string(8, 32)]
        self._test_equality_list_arg(self.audio.setTitle, self.audio.getTitle, test_arr)

    def test_album(self):
        test_arr = ["album1", "album2", generate_random_string(5, 20), "album4", generate_random_japanese_string(8, 32), generate_random_string(50, 200)]
        self._test_equality_list_arg(self.audio.setAlbum, self.audio.getAlbum, test_arr)

    def test_track_disc_number(self):
        disc, tot_discs, track, tot_tracks = 2, 5, 9, 55
        self.audio.setDiscNumbers(disc, tot_discs)
        self.audio.setTrackNumbers(track, tot_tracks)
        self.assertEqual(disc, self.audio.getDiscNumber())
        self.assertEqual(tot_discs, self.audio.getTotalDiscs())
        self.assertEqual(track, self.audio.getTrackNumber())
        self.assertEqual(tot_tracks, self.audio.getTotalTracks())

    def test_comment(self):
        test_arr = ["comment1", "find this album at vgmdb.net/damn_son", generate_random_string(5, 20), "album4", generate_random_japanese_string(8, 32), generate_random_string(50, 200)]
        self._test_equality_list_arg(self.audio.setComment, self.audio.getComment, test_arr)

    def test_date(self):
        test_arr = ["2001-7-3", "567-  4 /  14 ", "2023-9 -  4 ", "2023- 9", "1969 ", "  2007/11-6"]
        expected_arr = ["2001-07-03", "0567-04-14", "2023-09-04", "2023-09", "1969", "2007-11-06"]
        for i, x in enumerate(test_arr):
            self.audio.setDate(x)
            self.assertEqual(self.audio.getDate(), expected_arr[i])

    def test_catalog(self):
        test_arr = ["KSLA-0211", "UNCD-0021~0025", generate_random_string(10, 10)]
        self._test_equality_list_arg(self.audio.setCatalog, self.audio.getCatalog, test_arr)

    def test_custom_tags(self):
        key = "MY_TAG"

        def generateValueList():
            return [generate_random_string(5, 35), "My_value", "testing  ...", "damn son ", generate_random_japanese_string(10, 20), generate_random_string(5, 15), "last custom tag"]

        self._test_equality_custom_tag(key, generateValueList())
        self._test_equality_list_arg(self.audio.setCatalog, self.audio.getCatalog, generateValueList())
        self._test_equality_list_arg(self.audio.setDiscName, self.audio.getDiscName, generateValueList())
        self._test_equality_list_arg(self.audio.setBarcode, self.audio.getBarcode, generateValueList())

    def test_getting_information(self):
        self.assertIsInstance(self.audio.printInfo(), str)

    def test_setting_deleting_front_cover(self):
        self.audio.setPictureOfType(getRandomCoverImageData(), "Cover (front)")
        self.assertTrue(self.audio.hasPictureOfType("Cover (front)"))

        self.audio.deletePictureOfType("Cover (front)")
        self.assertFalse(self.audio.hasPictureOfType("Cover (front)"))

    def test_setting_multiple_pictures(self):
        """This test is not for m4a files because they don't support multiple pictures"""
        chosen_picture_types: list[pictureTypes] = list(get_args(pictureTypes))
        if self.single_cover_test:
            chosen_picture_types = [random.choice(chosen_picture_types)]
        else:
            chosen_picture_types = select_random_keys_from_list(chosen_picture_types)
        for picture_type in chosen_picture_types:
            self.audio.setPictureOfType(getRandomCoverImageData(), picture_type)

        for picture_type in chosen_picture_types:
            self.assertTrue(self.audio.hasPictureOfType(picture_type))

    def test_xx_save(self):
        """xx is prepended so that the audio file is saved at the end"""
        self.audio.save()

    def _test_equality_list_arg(self, setter: Callable[[list[Any]], None], getter: Callable[[], list[Any]], setter_arg: list[Any], expected: Optional[list[Any]] = None):
        if not expected:
            expected = setter_arg

        setter([])
        self.assertEqual([], getter())

        setter(setter_arg[0:1])
        self.assertEqual(expected[0:1], getter())

        setter(setter_arg)
        self.assertEqual(expected, getter())

    def _test_equality_custom_tag(self, key: str, val: list[str], expected: Optional[list[str]] = None):
        if not expected:
            expected = val

        self.audio.setCustomTag(key, [])
        self.assertEqual(self.audio.getCustomTag(key), [])

        self.audio.setCustomTag(key, val[0:1])
        self.assertEqual(self.audio.getCustomTag(key), expected[0:1])

        self.audio.setCustomTag(key, val)
        self.assertEqual(self.audio.getCustomTag(key), expected)


def copy_base_samples(force: bool = False):
    print("copying base samples to modified folder")
    os.makedirs(modifiedFolder, exist_ok=True)
    for file in os.listdir(baseFolder):
        file_path = os.path.join(baseFolder, file)
        modified_file_path = os.path.join(modifiedFolder, file)
        if not force and os.path.exists(modified_file_path):
            continue
        if os.path.isfile(file_path):
            shutil.copy(file_path, modifiedFolder)


def test_mutagen_wrapper():
    extensions = ["mp3", "flac", "m4a", "wav", "ogg", "opus"]
    for extension in extensions:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestMutagenWrapper)
        print(f"\nTesting {extension} file")
        filePath = os.path.join(modifiedFolder, f"{extension}_test.{extension}")
        global audioImpl, filePathImpl
        audioImpl = AudioFactory.buildAudioManager(filePath)
        audioImpl.clearTags()
        # audioImpl.save()
        filePathImpl = filePath
        unittest.TextTestRunner().run(suite)


copy_base_samples()
test_mutagen_wrapper()
