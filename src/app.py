import sys

sys.path.append("..")

from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from src.zip_lookup.zipcode.zipcode_lookup import ZipCode
from src.zip_lookup.utils.convert_pig_latin import convert_name_to_pig_latin

app = Flask(__name__)
api = Api(app)

result = ""


class GetZipInfo(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('firstname',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('lastname',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('zipcode',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = GetZipInfo.parser.parse_args()
        firstname = data['firstname']
        lastname = data['lastname']
        zipcode = data['zipcode']

        zipcode_obj = ZipCode(zipcode)
        county_list = zipcode_obj.get_county()
        county_str = ", ".join(county_list)

        result = f"{convert_name_to_pig_latin(firstname, lastname)}'s zip code" \
                 f" {zipcode} is in {county_str} County and has a population of {zipcode_obj.get_population()}"

        return result


api.add_resource(GetZipInfo, '/create_phrase')
app.run(port=6000)
