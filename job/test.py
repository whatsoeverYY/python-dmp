from llm.call_llm import get_answer
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from file_operator.write_file import write_file
from file_operator.read_file import read_file
from langchain_community.document_loaders import CSVLoader


file_path = "/Users/ever/workspace/data-management-platform-frontend/src/views/ClinicalResult/CtResult/detail/OutcomeMeasureInfoPage.tsx"
tm_file_path = "/Users/ever/workspace/data-management-platform-frontend/modules/tm"
file_content = "wrong content"
# csv_file_path=sys.argv[1]+sys.argv[2]+'/export.csv'
csv_file_path=tm_file_path+'/export.csv'
# csv_file_path = '/Users/ever/AI/test.csv'
# if sys.argv[1]:
#     file_content = read_file(csv_file_path)

# loader = CSVLoader(file_path=csv_file_path, source_column="数据库 Field 名称", encoding="utf-8-sig")
loader = CSVLoader(file_path=csv_file_path, encoding="utf-8")
docs = loader.load()
# for doc in docs:
#     print(doc.metadata.get('source'))

# print(get_answer("请列举出这个csv文件的所有列名：" + docs))
print(docs)
# write_file(file_path, 'a', file_content)