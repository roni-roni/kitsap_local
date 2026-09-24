import 'package:flutter/material.dart';

import '../../core/destinations.dart';
import '../../shared/placeholder_tab.dart';

/// Class 5: curated list from data/events.json.
/// Class 9: "add to device calendar".
class EventsScreen extends StatelessWidget {
  const EventsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const PlaceholderTab(tab: AppTab.events);
  }
}
