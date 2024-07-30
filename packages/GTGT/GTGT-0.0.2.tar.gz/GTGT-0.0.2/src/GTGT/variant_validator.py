from typing import Any, Dict, List, Union, cast
from .provider import Provider
from pydantic import BaseModel

payload = Dict[str, Any]


class Links(BaseModel):
    omim_ids: List[str]
    gene_symbol: str
    ensembl_gene_id: str
    uniprot: str
    decipher: str
    variant: str
    hgnc: str
    ucsc: str

    databases: List[str] = [
        "omim",
        "lovd",
        "gtex",
        "uniprot",
        "decipher",
        "clinvar",
        "hgnc",
        "ucsc",
        "gnomad",
        "stringdb",
    ]

    def url(self, field: str) -> Union[str, List[str]]:
        if field == "omim":
            urls = list()
            for id in self.omim_ids:
                url = f"https://www.omim.org/entry/{id}"
                urls.append(url)
            return urls
        elif field == "lovd":
            return f"https://databases.lovd.nl/shared/genes/{self.gene_symbol}"
        elif field == "gtex":
            return f"https://gtexportal.org/home/gene/{self.ensembl_gene_id}"
        elif field == "uniprot":
            return f"https://www.uniprot.org/uniprotkb/{self.uniprot}/entry"
        elif field == "decipher":
            return f"https://www.deciphergenomics.org/sequence-variant/{self.decipher}"
        elif field == "clinvar":
            return f"https://www.ncbi.nlm.nih.gov/clinvar/?term={self.variant}"
        elif field == "hgnc":
            return f"https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/{self.hgnc}"
        elif field == "ucsc":
            return f"https://genome.cse.ucsc.edu/cgi-bin/hgGene?hgg_gene={self.ucsc}"
        elif field == "gnomad":
            return f"https://gnomad.broadinstitute.org/variant/{self.decipher}?dataset=gnomad_r4"
        elif field == "stringdb":
            return f"https://string-db.org/cgi/network?identifiers={self.gene_symbol}"
        else:
            raise NotImplementedError(f"Unknown field: '{field}'")

    def url_dict(self) -> Dict[str, str]:
        """Create a flat dict with urls to all databases"""
        d = dict()

        for field in self.databases:
            # omim can contain a list of IDs
            if field == "omim":
                for i, url in enumerate(self.url(field), 1):
                    d[f"{field}_{i}"] = url
            else:
                d[field] = cast(str, self.url(field))

        return d


def lookup_variant(provider: Provider, variant: str, assembly: str = "hg38") -> Links:
    url = f"https://rest.variantvalidator.org/VariantValidator/variantvalidator/{assembly}/{variant}/mane_select?content-type=application/json"

    payload = provider.get(url)

    d = parse_payload(payload[variant], assembly)
    d["uniprot"] = lookup_uniprot(provider, d["ensembl_gene_id"])
    d["variant"] = variant

    return Links(**d)


def lookup_uniprot(provider: Provider, ensembl_gene_id: str) -> str:
    url = f"https://mygene.info/v3/gene/{ensembl_gene_id}?fields=uniprot"
    uniprot_id: str = provider.get(url)["uniprot"]["Swiss-Prot"]
    return uniprot_id


def parse_payload(payload: payload, assembly: str) -> payload:
    d = {
        "omim_ids": payload["gene_ids"]["omim_id"],
        "gene_symbol": payload["gene_symbol"],
        "ensembl_gene_id": payload["gene_ids"]["ensembl_gene_id"],
        "hgnc": payload["annotations"]["db_xref"]["hgnc"],
        "ucsc": payload["gene_ids"]["ucsc_id"],
    }
    # Get the 'VCF' notation on the specified assembly
    vcf = payload["primary_assembly_loci"][assembly]["vcf"]
    # Remove the 'chr' prefix
    vcf["chr"] = vcf["chr"][3:]
    # Decypher uses {chrom}-{pos}-{ref}-{alt} as variant ID
    d["decipher"] = "-".join(vcf[field] for field in ["chr", "pos", "ref", "alt"])
    return d
