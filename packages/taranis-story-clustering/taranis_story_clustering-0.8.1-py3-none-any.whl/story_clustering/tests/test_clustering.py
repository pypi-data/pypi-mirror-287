import json

expected_results = {"event_clusters": [["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"]]}
expected_results_inc = {"event_clusters": [["1", "1"], ["2", "2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"]]}


def test_create_corpus():
    from story_clustering.clustering import create_corpus
    from .testdata import news_item_list

    corpus = create_corpus(news_item_list)
    assert len(corpus.docs) == 8
    assert corpus.docs["1"].title == "Test News Item 13"
    assert "cve-2021-5678" in corpus.docs["2"].keywords.keys()


def test_initial_clustering():
    from story_clustering.clustering import initial_clustering
    from .testdata import news_item_list

    clustering_results = initial_clustering(news_item_list)
    print(clustering_results)
    assert set(map(tuple, clustering_results["event_clusters"])) == set(map(tuple, expected_results["event_clusters"]))


def test_incremental_clustering():
    from story_clustering.clustering import incremental_clustering_v2
    from .testdata import news_item_list, clustered_news_item_list

    clustering_results = incremental_clustering_v2(news_item_list, clustered_news_item_list)
    print(clustering_results)
    assert set(map(tuple, clustering_results["event_clusters"])) == set(map(tuple, expected_results_inc["event_clusters"]))


def test_incremental_clsutering_v2():
    from story_clustering.clustering import incremental_clustering_v2
    from .testdata import news_item_list, clustered_news_item_list

    clustering_results = incremental_clustering_v2(news_item_list, clustered_news_item_list)
    print(clustering_results)
    assert set(map(tuple, clustering_results["event_clusters"])) == set(map(tuple, expected_results_inc["event_clusters"]))


def test_dump_corpus():
    from story_clustering.clustering import create_corpus, extract_events_from_corpus
    from story_clustering.document_representation import CorpusEncoder, Corpus, Document

    from .testdata import news_item_list

    corpus = create_corpus(news_item_list)
    assert isinstance(corpus, Corpus)
    corpus_json = json.dumps(corpus, cls=CorpusEncoder)
    assert isinstance(corpus_json, str)
    corpus_dict = json.loads(corpus_json)
    assert isinstance(corpus_dict, dict)
    assert isinstance(corpus_dict["docs"], dict)
    rehydrated_corpus = Corpus(**corpus_dict)
    assert isinstance(rehydrated_corpus, Corpus)
    assert isinstance(rehydrated_corpus.docs["1"], Document)
    assert rehydrated_corpus.docs["1"].title == "Test News Item 13"
    events = extract_events_from_corpus(corpus=rehydrated_corpus)
    assert isinstance(events, list)
    assert len(events) == 8
