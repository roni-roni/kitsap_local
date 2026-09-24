import 'package:flutter/material.dart';

import '../core/destinations.dart';

/// Stand-in body for a tab that has no real content yet. Each feature screen
/// starts as one of these and is replaced in the class named on screen.
class PlaceholderTab extends StatelessWidget {
  const PlaceholderTab({required this.tab, super.key});

  final AppTab tab;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final colors = Theme.of(context).colorScheme;

    return Scaffold(
      appBar: AppBar(title: Text(tab.label)),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          Icon(tab.selectedIcon, size: 64, color: colors.primary),
          const SizedBox(height: 16),
          Text(
            'Coming in Class ${tab.arrivesInClass}',
            style: text.headlineSmall,
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 8),
          Text(
            tab.blurb,
            style: text.bodyLarge,
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 24),
          Text('Planned data sources', style: text.titleMedium),
          const SizedBox(height: 8),
          for (final source in tab.dataSources)
            ListTile(
              dense: true,
              contentPadding: EdgeInsets.zero,
              leading: const Icon(Icons.link, size: 18),
              title: Text(source),
            ),
        ],
      ),
    );
  }
}
