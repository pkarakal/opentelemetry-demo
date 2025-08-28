#!/usr/bin/python

# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0
from opentelemetry.metrics import Counter

def init_metrics(meter) -> tuple[Counter, Counter, Counter]:

    # Recommendations counter
    app_recommendations_counter = meter.create_counter(
        'app_recommendations_counter', unit='recommendations', description="Counts the total number of given recommendations"
    )

    app_recommendations_cache_misses = meter.create_counter(
        'app.recommendations.cache_misses', description="Counts the total number of cache misses"
    )

    app_recommendations_cache_hits = meter.create_counter(
        'app.recommendations.cache_hits', description="Counts the total number of cache hits"
    )

    return app_recommendations_counter, app_recommendations_cache_misses, app_recommendations_cache_hits
