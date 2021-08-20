from fastapi import FastAPI, Response

from aurorae.payroll.models import Payroll
from aurorae.providers.spreadsheet.models import Spreadsheet


app = FastAPI()


@app.post("/parse_from_spreadsheet")
async def parse_from_spreadsheet_data(spreadsheet_data: Spreadsheet):
    spreadsheet = Spreadsheet.parse_obj(spreadsheet_data)
    payroll = Payroll.parse_obj(spreadsheet.dict())

    cnab_file = payroll.get_cnab_file()
    response = cnab_file.as_fixed_width()

    return Response(content=response, media_type="text/html")
