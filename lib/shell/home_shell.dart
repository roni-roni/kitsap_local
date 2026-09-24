import 'package:flutter/material.dart';

import '../core/destinations.dart';
import '../features/bus/bus_screen.dart';
import '../features/events/events_screen.dart';
import '../features/ferry/ferry_screen.dart';
import '../features/government/government_screen.dart';
import '../features/help/help_screen.dart';
import '../features/parks/parks_screen.dart';

/// The six-tab shell: a bottom [NavigationBar] over an [IndexedStack].
///
/// IndexedStack keeps every tab alive, so scroll position and (later) map
/// camera survive switching tabs. The cost is that all six build up front,
/// a trade-off worth discussing in Class 3.
///
/// Class 4 replaces this hand-rolled state with go_router's
/// StatefulShellRoute, which gives the same behavior plus deep links.
class HomeShell extends StatefulWidget {
  const HomeShell({super.key});

  @override
  State<HomeShell> createState() => _HomeShellState();
}

class _HomeShellState extends State<HomeShell> {
  int _index = 0;

  // Order must match AppTab.values.
  static const List<Widget> _screens = [
    BusScreen(),
    FerryScreen(),
    GovernmentScreen(),
    ParksScreen(),
    EventsScreen(),
    HelpScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IndexedStack(index: _index, children: _screens),
      bottomNavigationBar: NavigationBar(
        selectedIndex: _index,
        onDestinationSelected: (i) => setState(() => _index = i),
        // Material 3 recommends 3-5 destinations; with six (seven once Jobs
        // ships) we show a label only on the selected one.
        labelBehavior: NavigationDestinationLabelBehavior.onlyShowSelected,
        destinations: [
          for (final tab in AppTab.values)
            NavigationDestination(
              icon: Icon(tab.icon),
              selectedIcon: Icon(tab.selectedIcon),
              label: tab.label,
            ),
        ],
      ),
    );
  }
}
