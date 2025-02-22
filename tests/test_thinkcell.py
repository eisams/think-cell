import pytest
from thinkcell import Thinkcell
from datetime import datetime
import os


class TestThinkcell(object):
    def test_init(self):
        tc = Thinkcell()
        assert tc.charts == []

    def test_str_all(self):
        tc = Thinkcell()
        assert str(tc) == "[]"

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("daf", {"string": "daf"}),
            (3, {"number": 3}),
            (2.0, {"number": 2.0}),
            (datetime(2012, 9, 16, 0, 0), {"date": "2012-09-16"}),
        ],
    )
    def test_transform_input(self, test_input, expected):
        assert Thinkcell.transform_input(test_input) == expected

    def test_transform_input_bad(self):
        with pytest.raises(ValueError) as e_info:
            Thinkcell.transform_input([3, 4])

    def test_verify_template_1(self):
        template_name = "not a file name"
        with pytest.raises(TypeError) as e_info:
            Thinkcell.verify_template(template_name)

    def test_verify_template_2(self):
        template_name = 5
        with pytest.raises(TypeError) as e_info:
            Thinkcell.verify_template(template_name)

    def test_verify_template_3(self):
        template_name = "example.pptx"
        assert Thinkcell.verify_template(template_name) == template_name

    def test_add_template(self):
        tc = Thinkcell()
        template = "example.pptx"
        tc.add_template(template)
        assert tc.charts == [{"template": template, "data": []}]

    def test_add_chart_warning(self):
        tc = Thinkcell()
        template_name = "template.pptx"
        tc.add_template(template_name)
        with pytest.warns(UserWarning) as record:
            tc.add_chart(
                template_name=template_name,
                chart_name=234,
                categories=["Alpha", "bravo"],
                data=[[3, 4, datetime(2012, 9, 16, 0, 0)], [2, "adokf", 6]],
            )

    def test_add_chart_bad_template(self):
        tc = Thinkcell()
        template = "example.pptx"
        with pytest.raises(ValueError) as e_info:
            tc.add_chart(
                template_name="example2.pptx",
                chart_name="Cool Name bro",
                categories=["Alpha", "bravo"],
                data=[[3, 4, datetime(2012, 9, 16, 0, 0)], [2, "adokf", 6]],
            )

    def test_add_chart_bad_dimensions(self):
        tc = Thinkcell()
        template_name = "example.pptx"
        tc.add_template(template_name)
        with pytest.raises(ValueError) as e_info:

            tc.add_chart(
                template_name=template_name,
                chart_name="Cool Name bro",
                categories=["Alpha", "bravo"],
                data=[[3, 4, datetime(2012, 9, 16, 0, 0)], [2, "adokf"]],
            )

    def test_add_chart(self):
        tc = Thinkcell()
        template = "example.pptx"
        tc.add_template(template)
        tc.add_chart(
            template_name=template,
            chart_name="Cool Name bro",
            categories=["Alpha", "bravo"],
            data=[[3, 4, datetime(2012, 9, 16, 0, 0)], [2, "adokf", 4]],
        )
        assert tc.charts == [
            {
                "template": "example.pptx",
                "data": [
                    {
                        "name": "Cool Name bro",
                        "table": [
                            [None, {"string": "Alpha"}, {"string": "bravo"}],
                            [],
                            [
                                {"number": 3},
                                {"number": 4},
                                {"date": "2012-09-16"},
                            ],
                            [
                                {"number": 2},
                                {"string": "adokf"},
                                {"number": 4},
                            ],
                        ],
                    }
                ],
            }
        ]

    @pytest.mark.parametrize(
        "input, output", [("word.docx", ValueError), (3, ValueError)]
    )
    def test_save_ppttc_bad_file(self, input, output):
        tc = Thinkcell()
        tc.add_template("example.pptx")
        tc.add_chart(
            template_name="example.pptx",
            chart_name="Chart name",
            categories=["alpha", "bravo"],
            data=[["today", 1, 2], ["tomorrow", 3, 4]],
        )
        with pytest.raises(output) as e_info:
            tc.save_ppttc(filename=input)

    def test_save_pptc(self):
        tc = Thinkcell()
        with pytest.raises(ValueError) as e_info:
            tc.save_ppttc("test.ppttc")

    def test_save_ppttc(self):
        tc = Thinkcell()
        tc.add_template("example.pptx")
        tc.add_chart(
            template_name="example.pptx",
            chart_name="Chart name",
            categories=["alpha", "bravo"],
            data=[["today", 1, 2], ["tomorrow", 3, 4]],
        )
        assert tc.save_ppttc(filename="test.ppttc") == True
        os.remove("test.ppttc")
