import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:kitsap_local/app.dart';
import 'package:kitsap_local/core/destinations.dart';

void main() {
  testWidgets('shell has six tabs and each one opens its screen', (
    tester,
  ) async {
    await tester.pumpWidget(const KitsapApp());

    expect(find.byType(NavigationDestination), findsNWidgets(6));
    expect(AppTab.values, hasLength(6));

    for (var i = 0; i < AppTab.values.length; i++) {
      await tester.tap(find.byType(NavigationDestination).at(i));
      await tester.pumpAndSettle();

      // Only the visible tab's AppBar is on stage (IndexedStack hides the rest).
      expect(
        find.descendant(
          of: find.byType(AppBar),
          matching: find.text(AppTab.values[i].label),
        ),
        findsOneWidget,
      );
    }
  });
}
