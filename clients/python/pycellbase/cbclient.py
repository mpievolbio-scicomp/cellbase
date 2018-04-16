import pycellbase.cbrestclients as crc
from pycellbase.cbconfig import ConfigClient
from pycellbase.commons import get


class CellBaseClient(object):
    """Creates different query clients and allows direct queries to the RESTful
     service"""
    def __init__(self, config_client=None):
        # CellBase REST clients
        self._gene_client = None
        self._transcript_client = None
        self._protein_client = None
        self._variation_client = None
        self._xref_client = None
        self._genomic_region_client = None
        self._variant_client = None
        self._genome_sequence_client = None
        self._clinical_client = None
        self._meta_client = None

        # Setting up config params
        if config_client is not None:
            if isinstance(config_client, ConfigClient):
                self._configuration = config_client
            else:
                msg = ('CellBaseClient configuration not properly set.' +
                       ' "pycellbase.config.ConfigClient" object is needed as' +
                       ' parameter')
                raise ValueError(msg)
        else:
            self._configuration = ConfigClient()

    def show_configuration(self):
        """Returns current configuration parameters"""
        return self._configuration.configuration

    def get_default_configuration(self):
        return self._configuration.get_default_configuration()

    def get(self, category, subcategory, resource, query_id=None, **options):
        """Creates the URL for querying the REST service"""
        response = get(host=self._configuration.host,
                       version=self._configuration.version,
                       species=self._configuration.species,
                       category=category,
                       subcategory=subcategory,
                       query_id=query_id,
                       resource=resource,
                       options=options)
        return response

    def get_gene_client(self):
        """Creates the gene client"""
        if self._gene_client is None:
            self._gene_client = crc.GeneClient(self._configuration)
        return self._gene_client

    def get_transcript_client(self):
        """Creates the protein client"""
        if self._transcript_client is None:
            self._transcript_client = crc.TranscriptClient(self._configuration)
        return self._transcript_client

    def get_protein_client(self):
        """Creates the protein client"""
        if self._protein_client is None:
            self._protein_client = crc.ProteinClient(self._configuration)
        return self._protein_client

    def get_variation_client(self):
        """Creates the variation client"""
        if self._variation_client is None:
            self._variation_client = crc.VariationClient(self._configuration)
        return self._variation_client

    def get_xref_client(self):
        """Creates the xref client"""
        if self._xref_client is None:
            self._xref_client = crc.XrefClient(self._configuration)
        return self._xref_client

    def get_genomic_region_client(self):
        """Creates the genomic region client"""
        if self._genomic_region_client is None:
            self._genomic_region_client = \
                crc.GenomicRegionClient(self._configuration)
        return self._genomic_region_client

    def get_variant_client(self):
        """Creates the variant client"""
        if self._variant_client is None:
            self._variant_client = crc.VariantClient(self._configuration)
        return self._variant_client

    def get_genome_sequence_client(self):
        """Creates the genome sequence client"""
        if self._genome_sequence_client is None:
            self._genome_sequence_client = \
                crc.GenomeSequenceClient(self._configuration)
        return self._genome_sequence_client

    def get_clinical_client(self):
        """Creates the clinical client"""
        if self._clinical_client is None:
            self._clinical_client = crc.ClinicalClient(self._configuration)
        return self._clinical_client

    def get_meta_client(self):
        """Creates the clinical client"""
        if self._meta_client is None:
            self._meta_client = crc.MetaClient(self._configuration)
        return self._meta_client
