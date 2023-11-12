import re
import apache_beam as beam
from datetime import datetime
from configuration import MONGO_COLLECTION, MONGO_HOST, MONGO_PORT, MONGO_DB
from connectivity.web_scraper import WebScraper


class TwitterProcessor:
    """
    This is the main class in . It utilizes apache beam to create batch pipelines to process the captured data.
    It includes separating the twits, applying quality rule, generating the documents and inserting into Mongo DB.
    """

    @staticmethod
    def run(data):
        with beam.Pipeline() as pipeline:
            outputs = (
                pipeline
                | 'Create values' >> beam.Create(data)
                | 'Separate Twits' >> beam.FlatMap(lambda x: x.split("\n"))
                | 'Filter Empty Lines' >> beam.Filter(lambda x: x != "")
                | 'Process Twits' >> beam.Map(lambda x: TwitterProcessor.process_twit(x))
                | 'Group Twits' >> beam.GroupByKey()
                | 'Generate Documents' >> beam.Map(TwitterProcessor.generate_document)
                | 'Write To Mongo' >> beam.io.mongodbio.WriteToMongoDB(
                    uri=f'mongodb://{MONGO_HOST}:{MONGO_PORT}',
                    db=MONGO_DB,
                    coll=MONGO_COLLECTION,
                    batch_size=100)
            )

            outputs | beam.Map(print)

    @staticmethod
    def process_twit(twit: str):
        """
        Process a twit applying quality rules.
        """
        twit = twit.replace("RT:", "")  # Remove RT
        twit = twit.replace("#", "")  # Remove #
        twit = twit.strip()  # Remove leading / trailing spaces
        twit = " ".join(twit.split())  # Remove double spaces
        twit = re.sub(r'http://\S+|https://\S+', '', twit, flags=re.MULTILINE)  # Remove URLs
        return "twit", twit

    @staticmethod
    def generate_document(twits):
        """
        Generate a dict (json like document) to be inserted in Mongo.
        """
        document = {
            "content": twits[1],
            "timestamp": datetime.now(),
            "total_case_count": WebScraper.get_covid_cases()
        }
        return document
